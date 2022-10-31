from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import numpy as np
from pydantic import BaseModel
import torch
from fastapi import Request, FastAPI
model_name = 'google/pegasus-large'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)

class Input_Text(BaseModel):
    text: str
    

app = FastAPI()

@app.get("/")
def home():
    return {"message":"working i guess"}


@app.post("/get_pegasus/")
def pegasus_text(in_text : Input_Text):
    return {"pegasus_summary" :pegasus_fn(in_text.text)}

def pegasus_fn(src_text):
  src_text = src_text.replace('"', '')
  batch = tokenizer(src_text, truncation=True, padding='longest', return_tensors="pt").to(device)
  translated = model.generate(**batch)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text


  