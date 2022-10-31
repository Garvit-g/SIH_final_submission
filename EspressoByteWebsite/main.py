from typing import Optional
from fastapi import Request, FastAPI
import nltk
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
from nltk.tokenize import sent_tokenize
import networkx as nx
import re
import numpy as np
from pydantic import BaseModel
import openai
from newspaper import Article

class Input_Text(BaseModel):
    text: str

class Input_Url(BaseModel):
    url: str

app = FastAPI()

@app.get("/")
def home():
    return {"message":"wokring i guess"}

@app.post("/open_ai_summarise_url/")
def summarise_text(in_url: Input_Url):
    text = get_text_from_url(in_url.url)
    return {"summary_from_url" : openai_summary(text)}

@app.post("/open_ai_summarise_text/")
def summarise_text(in_text : Input_Text):
    return {"summary" : openai_summary(in_text.text)}

@app.post("/bow_summarise_url/")
def summarise_text(in_url: Input_Url):
    text = get_text_from_url(in_url.url)
    return {"summary_from_url" : nk_sir_summary(text)}

@app.post("/bow_summarise_text/")
def summarise_text(in_text : Input_Text):
    return {"summary" : nk_sir_summary(in_text.text)}

@app.post("/second_summarise_url/")
def summarise_text(in_url: Input_Url):
    text = get_text_from_url(in_url.url)
    return {"summary_from_url" : second_nk_algo(text)}

@app.post("/second_summarise_text/")
def summarise_text(in_text : Input_Text):
    return {"summary" : second_nk_algo(in_text.text)}

def casefolding(sentence):
    return sentence.lower()

def cleaning(sentence):
    return re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))

def tokenization(sentence):
    return sentence.split()
 
def sentence_split(paragraph):
    return nltk.sent_tokenize(paragraph)

# Read the text and tokenize into sentences
def read_article(text):
    
    sentences =[]
    
    sentences = sent_tokenize(text)
    for sentence in sentences:
        sentence.replace("[^a-zA-Z0-9]"," ")

    return sentences
    

# Create vectors and calculate cosine similarity b/w two sentences
def sentence_similarity(sent1,sent2,stopwords=None):
    if stopwords is None:
        stopwords = []
    
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
    
    all_words = list(set(sent1 + sent2))
    
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    
    #build the vector for the first sentence
    for w in sent1:
        if not w in stopwords:
            vector1[all_words.index(w)]+=1
    
    #build the vector for the second sentence
    for w in sent2:
        if not w in stopwords:
            vector2[all_words.index(w)]+=1
            
    return 1-cosine_distance(vector1,vector2)

# Create similarity matrix among all sentences
def build_similarity_matrix(sentences,stop_words):
    #create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences),len(sentences)))
    
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1!=idx2:
                similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1],sentences[idx2],stop_words)
                
    return similarity_matrix


# Generate and return text summary
def second_nk_algo(text, top_n=2):
    stop_words = stopwords.words('english')
    summarize_text = []
    
    # Step1: read text and tokenize
    sentences = read_article(text)
    
    # Steo2: generate similarity matrix across sentences
    sentence_similarity_matrix = build_similarity_matrix(sentences,stop_words)
    
    # Step3: Rank sentences in similarirty matrix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    
    #Step4: sort the rank and place top sentences
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)),reverse=True)
    
    # Step 5: get the top n number of sentences based on rank    
    for i in range(top_n):
        summarize_text.append(ranked_sentences[i][1])
    
    # Step 6 : outpur the summarized version
    return " ".join(summarize_text)
    
def word_freq(data):
    w = []
    for sentence in data:
        for words in sentence:
            w.append(words)
    bag = list(set(w))
    res = {}
    for word in bag:
        res[word] = w.count(word)
    return res
    
def sentence_weight(data, wordfreq):
    weights = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        weights.append(temp)
    return weights

def nk_sir_summary(text):
    sentence_list = sentence_split(text) #cutting into sentence form, each sent prepro
    data = []
    for sentence in sentence_list:
        data.append(tokenization(cleaning(casefolding(sentence))))

    data = (list(filter(None, data)))

    wordfreq = word_freq(data)#count each word

    rank = sentence_weight(data, wordfreq)#weight of each sentence

    n = 2 #no of main sentences to output; system takes top n sentences of highest weight
    result = ''
    sort_list = np.argsort(rank)[::-1][:n]
    for i in range(n):
        result += '{} '.format(sentence_list[sort_list[i]])

    return result

def openai_summary(paperContent):
    tldr_tag = "\n tl;dr:"
    openai.organization = 'org-9rbTVUqetC666xwjyOrBz0A6'
    openai.api_key = "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"
    engine_list = openai.Engine.list() 
    
    paperContent += tldr_tag
    
    response = openai.Completion.create(engine="davinci",prompt=paperContent,temperature=0.7,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return (response["choices"][0]["text"])

def get_text_from_url(url):
    """https://sih-hackathon-api.herokuapp.com/
    Parses the information in the given url and returns the text from it
    Parameters:
        url (string) : URL to an article
    Returns:
        string : Text from article
    """
    article = Article(url, language="en")
    article.download()
    article.parse()
    return article.text
