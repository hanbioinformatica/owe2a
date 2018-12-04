import urllib.request
import re

url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'
url = "http://nu.nl"
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<a href="(http.*?)"',str(respData))

for eachP in paragraphs:
    print(eachP)
