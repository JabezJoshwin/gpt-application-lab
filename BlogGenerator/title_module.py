from utils import ModelError
def generate_titles(client,data):
    result=client.generate('Generate exactly five distinct attractive titles for the supplied blog. Return JSON with a titles array of five strings.',data,True)
    titles=result.get("titles") if isinstance(result,dict) else None
    if not isinstance(titles,list) or len(titles)!=5 or any(not isinstance(t,str) or not t.strip() for t in titles) or len(set(t.casefold() for t in titles))!=5:
        raise ModelError("Model must return five distinct non-empty titles")
    return "\n".join(f"{i}. {title}" for i,title in enumerate(titles,1))
