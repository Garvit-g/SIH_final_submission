import nltk 
from nltk.corpus import stopwords 
#nltk.download()
from nltk.tokenize import word_tokenize, sent_tokenize

def ProperNounExtractor(text):
    arr = []
    print('PROPER NOUNS EXTRACTED :')
    
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if tag == 'NNP': # If the word is a proper noun
                arr.append(word)
    for w in arr:
        text.replace(w, '#'+w)
text =  "Rohan is a wonderful player. He was born in India. He is a fan of the movie Wolverine. He has a dog named Bruno."
# Calling the ProperNounExtractor function to extract all the proper nouns from the given text. 
ProperNounExtractor(text)

