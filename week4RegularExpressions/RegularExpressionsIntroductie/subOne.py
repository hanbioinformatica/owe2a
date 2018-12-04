import re

tekst = "mobiel: 06-94324233"

telefoonnummer = re.sub(r"\D","", tekst)

print (telefoonnummer)



