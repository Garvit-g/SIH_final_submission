!pip install git+https://github.com/PrithivirajDamodaran/Styleformer.git

from styleformer import Styleformer
import torch

#Passive to Active
sf = Styleformer(style = 3) 

import nltk
nltk.download('punkt')
from nltk import tokenize

from fastapi import Request, FastAPI
from pydantic import BaseModel

class Input_Text(BaseModel):
    text: str
    

app = FastAPI()

@app.get("/")
def home():
    return {"message":"working i guess"}


@app.post("/get_active/")
def active_text(in_text : Input_Text):
    return {"translation" :active_fn(in_text.text)}

def active_fn(text):
  source_sentences= tokenize.sent_tokenize(text)
  output=""
  for source_sentence in source_sentences:
    output = output+((sf.transfer(source_sentence))).capitalize()+' '
  return output

