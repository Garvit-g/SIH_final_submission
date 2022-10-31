
def transformer_summary(in_text : Input_Text):
    return {"translation" :summarize_bert(in_text.text, 200, 30)}

@app.post("/summary_from_url/")
def get_sum_article(in_url: Input_Url):
    text = get_summary_link(in_url.url)
    return {"summary" : text}

def summarize_bert(text,max_length=200,min_length=30):
  return summarizer(text, max_length=200, min_length=30, do_sample=False)

def get_summary_link():
    article = Article(url, language="en")
    article.download()
    article.parse()
    return summarize_bert(article.text, 200, 30)