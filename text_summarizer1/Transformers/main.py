from transformers import pipeline
from fastapi import Request, FastAPI
import numpy as np
from pydantic import BaseModel
from newspaper import Article
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class Input_Text(BaseModel):
    text: str

class Input_Url(BaseModel):
    url: str

from fastapi.middleware.cors import CORSMiddleware

   
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

@app.get("/")
def home():
    return {"message":"working i guess"}


@app.post("/transformer/")
def transformer_summary(in_text : Input_Text):
    return summarize_bert(in_text.text, 200, 30)

@app.post("/summary_from_url/")
def get_sum_article(in_url: Input_Url):
    text = get_summary_link(in_url.url)
    return text

def summarize_bert(text,max_length,min_length):
  return summarizer(text, 300,int(0.1*len(text.split())) , do_sample=False,truncation=True)[0]

def get_summary_link(url):
    article = Article(url, language="en")
    article.download()
    article.parse()
    print(article.text)
    return summarize_bert(article.text, 200, 30)