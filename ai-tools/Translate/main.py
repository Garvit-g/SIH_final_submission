from fastapi import Request, FastAPI
import numpy as np
from pydantic import BaseModel
import googletrans
from googletrans import Translator
tr = Translator()

class Input_Text(BaseModel):
    text: str
    src: str
    dest: str

app = FastAPI()

@app.get("/")
def home():
    return {"message":"working i guess"}


@app.post("/get_translation/")
def translate_text(in_text : Input_Text):
    return {"translation" :translate_fn(in_text.text, in_text.src, in_text.dest)}

def translate_fn(text, srclang, destlang):
  result = tr.translate(text, src = srclang, dest=destlang)
  return result.text