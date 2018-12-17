"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van recursie voor het omdraaien van een woord
Creatie d.d. 17 december 2018

"""


def main():
    tekst = rreverse("Hello World!")
    print (tekst)

def rreverse(s):
    if s == "":
        return s
    else:
        return s[-1] + rreverse(s[:-1])

main()
