# !/usr/bin/env python

"""Martijn van der Bruggen
HAN University 2007
Aangepast aan nieuwe opzet Google d.d. 8-feb-2010

TITLE:       readingHTTPgoogle.py
VERSION:     0.1 alpha
AUTHOR:      Martijn van der Bruggen <Martijn.vanderBruggen@han.nl>
COPYRIGHT:   HAN University of Applied Science
DESCRIPTION: A python wrapper for google
USAGE:       Run the script and get the count for a search term
DATE:        Januari 2007
UPDATED:     November 2010, corrected new HTML tags for Google
UPDATED:     December 2011, converted to Python 3 code
UPDATED:     December 2011, corrected new HTML tags for Google about <b> and for
UPDATED:     December 2012, corrected new HTML tags for google about and results<nobr>
UPDATED:     February 2013, upgrade to MatPlotLib for Python 3
UPDATED:     November 2018, corrected for new Google format
UPDATED:     November 2018, structured conform PEP8
"""

# Import the http library
import urllib
from pylab import *
from urllib.request import Request

def main():
    labels = ['Frans', 'Python', 'Duits']
    waardes = getList(labels)
    tekenGrafiek(labels, waardes)


def getCount(term):
    # Define server, path and term to search
    begin = "<h2 class=\"figure\">".lower()
    eind = "vacatures gevonden".lower()
    hits = ""
    # Start Connection and get response
    url ="https://www.monsterboard.nl/vacatures/zoeken/?q=" + term
    print (url)
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    fp = urllib.request.urlopen(req)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    # # Start reading and analyzing HTML
    data1 = str(mystr.lower())
    pos1 = data1.index(begin)
    pos2 = data1.index(eind)
    tekst = data1[pos1 + len(begin):pos2]
    for c in tekst:
        if c in "0123456789":
            hits += c
    getal = int(hits)
    return getal


def getList(zoekwoordenlijst):
    data = []  # List met waardes voor de Y-as
    maxScore = 0
    for label in zoekwoordenlijst:
        c = getCount(label.replace(' ', '+'))
        if c > maxScore:
            maxScore = c
        print(label, c)
        data += [c]
    return data


def tekenGrafiek(labels, data):
    xlocations = range(len(data))  # List met x-as data
    breedte = 0.15  # Breedte van de lijn
    bar(xlocations, data, width=breedte)  # Tekenen van de grafiek
    xticks(xlocations, labels)
    xlim(0, xlocations[-1] + breedte * 2)
    title("HAN Job Counter")
    gca().get_xaxis().tick_bottom()
    gca().get_yaxis().tick_left()
    show()  # Toon de grafiek


main()
