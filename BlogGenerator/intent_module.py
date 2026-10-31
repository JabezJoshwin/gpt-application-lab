INTENTS=["BLOG_GENERATION","SUMMARY","KEYWORD_GENERATION","META_DESCRIPTION","TITLE_GENERATION","EXIT"]
def detect_intent(client,text):
    return client.classify(text,INTENTS)
