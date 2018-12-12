"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van OO aan de hand van een Auto
BIN-1c/Bin-1d
Creatie d.d. 12 december 2018
Aanpassingen d.d. 13 december 2018:
* __str__ methode toegevoegd


"""

class Auto:

    __max_snelheid = 130 # class variabele: voor alle objecten hetzelfde
    __aantal = 0  # class variabele

    # Constructor
    def __init__(self,e,v):
        print("Creatie van Object Auto")
        self.setEigenaar(e)
        self.setSnelheid(v)
        Auto.__aantal += 1
        print("Aantal Auto's{}".format(Auto.__aantal))


    # Functie die aangeroepen wordt als het object
    # wordt geprint Bijv. print (a1)
    def __str__(self):
        return "Auto van {}".format(self.eigenaar)

    def setEigenaar(self, e):
        self.eigenaar = e

    def getEigenaar(self):
        return self.eigenaar

    def setSnelheid(self,v):
        if v>Auto.__max_snelheid:
            print ("Dat mag niet {}".format(self.eigenaar))
            self.__snelheid = 0
        else:
            self.__snelheid = v

    def getSnelheid(self):
        return self.__snelheid

    def info(self):
        return "Auto van {} met een snelheid van {}"\
            .format(self.eigenaar, self.__snelheid)



# Hier begint de applicatie
# Die normaal in een appart bestand zou staan

a1 = Auto("Marnick",180)
a2 = Auto("Ronald",200)
a3 = Auto("Kim",100)

print(a1.info())
print(a2.info())
print(a3.info())

print (a1)
