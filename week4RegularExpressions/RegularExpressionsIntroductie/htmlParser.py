import urllib.request
import re

"""
Voorbeeld van 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'
Aangepast 2 december 2018 MvdB (c) HAN University of Applied Science
"""

def main ():
    data = getData ("http://nu.nl")
    links = getLinks(data)
    print (links)

def getData(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    return resp.read()

def getLinks(data):
    links = []
    hlinks = re.findall(r'<a href="(http.*?)"', str(data))
    for eachLink in hlinks:
        links.append(eachLink)
    return links

main()



