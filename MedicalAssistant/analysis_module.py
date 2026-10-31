from symptom_module import extract
from context_module import missing
from prompt_module import build_prompt,FIELDS
from safety_module import DISCLAIMER,guidance
from utils import structured
def analyze(client,profile):
    symptoms=extract(client,profile["symptoms"])
    result=structured(client.generate(build_prompt(),{"patient":profile,"symptoms":symptoms,"missing":missing(profile)},True),FIELDS)
    return {"Reported Symptoms":symptoms,"Patient Information":profile,**result,"Medical Attention Guidance":guidance(profile),"Disclaimer":DISCLAIMER}
