def missing(profile):
    return [k for k,v in profile.items() if v=="Not provided"] + ["Measured temperature if relevant","Whether symptoms are improving or worsening","Breathing difficulty or other concerning symptoms"]
