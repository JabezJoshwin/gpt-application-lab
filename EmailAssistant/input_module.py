from utils import required
def validate(data):
    return {k:required(data.get(k),k) for k in ("customer_name","subject","email")}
def collect():
    return validate({k:input(k.replace("_"," ")+": ") for k in ("customer_name","subject","email")})
