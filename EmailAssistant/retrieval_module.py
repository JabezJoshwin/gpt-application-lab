import csv,math,re
from collections import Counter
def words(text):return re.findall(r"[a-z0-9]+",text.lower())
def load_history(path):
    with open(path,encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f))
    if not rows or not {"email","reply"}.issubset(rows[0]):raise ValueError("CSV requires email and reply columns")
    return rows
def retrieve(query,rows):
    if not rows:return None
    docs=[words(r["email"]) for r in rows];n=len(docs)
    df=Counter(w for doc in docs for w in set(doc))
    def vector(tokens):return {w:c*(math.log((1+n)/(1+df[w]))+1) for w,c in Counter(tokens).items()}
    q=vector(words(query))
    def score(doc):
        v=vector(doc);den=math.sqrt(sum(x*x for x in q.values())*sum(x*x for x in v.values()))
        return sum(x*v.get(w,0) for w,x in q.items())/den if den else 0
    ranked=sorted(((score(d),i) for i,d in enumerate(docs)),reverse=True)
    similarity,index=ranked[0]
    return {**rows[index],"similarity":round(similarity,4)} if similarity>0 else None
