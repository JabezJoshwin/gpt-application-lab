from utils import required,integer
def validate(data):
    result={k:required(data.get(k),k) for k in ("name","background","interests","skill_level","preferred_category","goal")}
    result["age"]=integer(data.get("age"),"age",1,120);result["count"]=integer(data.get("count"),"count",1,10)
    result["constraints"]=str(data.get("constraints","None specified"))
    if not any(x.strip() for x in result["interests"].split(",")):raise ValueError("Enter at least one interest")
    return result
def analyze(profile):
    interests=[x.strip() for x in profile["interests"].split(",") if x.strip()]
    return {"primary_interest":interests[0],"secondary_interests":interests[1:],"skill_level":profile["skill_level"],"goal":profile["goal"],"preferred_type":profile["preferred_category"],"constraints":profile["constraints"]}
