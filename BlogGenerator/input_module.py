from utils import required, integer
def validate(data):
    return {**{k:required(data.get(k),k) for k in ("topic","style","tone")},"word_count":integer(data.get("word_count"),"word count",100,3000)}
def collect():
    return validate({k:input(k.replace("_"," ")+": ") for k in ("topic","style","tone","word_count")})
