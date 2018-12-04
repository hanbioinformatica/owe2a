import re
line="AGGGGCCACATTAATGATGGAGTATAGGAGTA"
matchObj = re.search(r"ATG",line)
print (matchObj.start())
print (matchObj.end())
print (matchObj.group())
