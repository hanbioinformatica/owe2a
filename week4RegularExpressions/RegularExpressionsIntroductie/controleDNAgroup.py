# Voorbeeld van https://pythonforbiologists.com/regular-expressions/
import re
dna = "TGGAXGCCAYCAWATGGAG"

matches = re.finditer(r"[^ATGC]", dna)
for matchObj in matches:
    base = matchObj.group()
    pos  = matchObj.start()
    print(base + " found at position " + str(pos))
