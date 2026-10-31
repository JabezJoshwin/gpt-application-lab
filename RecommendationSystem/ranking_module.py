from utils import ModelError
def rank(result,count):
    items=result.get("recommendations") if isinstance(result,dict) else None
    if not isinstance(items,list) or len(items)!=count:raise ModelError("Wrong recommendation count")
    seen=set()
    for item in items:
        if not isinstance(item,dict) or not all(isinstance(item.get(k),str) and item[k].strip() for k in ("name","reason")):raise ModelError("Invalid recommendation")
        score=item.get("score")
        if isinstance(score,bool) or not isinstance(score,(int,float)) or not 0<=score<=100:raise ModelError("Invalid suitability score")
        if item["name"].casefold() in seen:raise ModelError("Duplicate recommendation")
        seen.add(item["name"].casefold())
    return sorted(items,key=lambda x:x["score"],reverse=True)
