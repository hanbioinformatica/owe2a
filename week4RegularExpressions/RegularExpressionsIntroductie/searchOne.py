import re
line="AGGGGCCACATTAATGATGGAGTATAGGAGTA"
matchObj = re.search(r"G[ATG]{2,4}A",line)
print (matchObj)
print (matchObj.start())
print (matchObj.end())
print (matchObj.group())
