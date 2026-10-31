from profile_module import validate
def collect():return validate({k:input(k.replace("_"," ")+": ") for k in ("name","age","background","interests","skill_level","preferred_category","goal","count","constraints")})
