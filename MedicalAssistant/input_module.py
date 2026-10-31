from profile_module import validate
def collect():return validate({k:input(k+": ") for k in ("age","sex","symptoms","duration","severity","history","medications","allergies")})
