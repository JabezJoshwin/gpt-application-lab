from utils import integer,required
def validate(data):
    result={k:str(data.get(k,"Not provided")).strip() or "Not provided" for k in ("sex","history","medications","allergies")}
    result["age"]=integer(data.get("age"),"age",0,120)
    result["symptoms"]=required(data.get("symptoms"),"symptoms")
    result["duration"]=required(data.get("duration"),"duration")
    result["severity"]=required(data.get("severity"),"severity")
    if result["severity"].lower() not in ("mild","moderate","severe","unknown"):raise ValueError("Severity: mild/moderate/severe/unknown")
    return result
