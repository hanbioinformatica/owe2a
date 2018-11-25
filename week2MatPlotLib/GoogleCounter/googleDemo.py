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
import http.client
from pylab import *


def main():
    labels = ['"Donald Trump"', '"Barack Obama"', '"Theresa May"']
    waardes = getList(labels)
    tekenGrafiek(labels, waardes)


def getCount(google_term):
    # Define server, path and term to search
    google_server = "www.google.com"
    google_path = "/search?hl=en&q="
    begin = "about ".lower()
    eind = "results</div>".lower()
    hits = ""

    # Start Connection and get response
    conn = http.client.HTTPConnection(google_server)
    conn.request("GET", google_path + google_term)
    r1 = conn.getresponse()
    # Start reading and analyzing HTML
    data1 = str(r1.read().lower())
    pos1 = data1.index(begin)
    pos2 = data1.index(eind)
    tekst = data1[pos1 + len(begin):pos2]
    for c in tekst:
        if c in "0123456789":
            hits += c
    getal = int(hits)
    conn.close()
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
    breedte = 0.1  # Breedte van de lijn
    bar(xlocations, data, width=breedte)  # Tekenen van de grafiek
    xticks(xlocations, labels)
    xlim(0, xlocations[-1] + breedte * 2)
    title("HAN Google Counter")
    gca().get_xaxis().tick_bottom()
    gca().get_yaxis().tick_left()
    show()  # Toon de grafiek


main()
