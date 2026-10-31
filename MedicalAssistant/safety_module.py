DISCLAIMER="""This AI-generated response is intended for educational and informational purposes only.
It is not a medical diagnosis and does not replace advice from a qualified healthcare professional.
For serious, worsening or urgent symptoms, seek appropriate medical care."""
GUIDANCE="If symptoms are severe, rapidly worsening, or concerning, seek appropriate professional medical care. This application does not make clinical triage decisions."
def guidance(profile):
    return GUIDANCE + (" You reported severe symptoms; seek appropriate professional medical care." if profile["severity"].lower()=="severe" else "")
