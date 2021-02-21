import re 

pattern = re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}\d")
password = "penurai22"

a = pattern.fullmatch(password)
print(a)

