"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van OO aan de hand van een Auto
BIN-1c/Bin-1d
Creatie d.d. 12 december 2018

"""

class Auto:

    __max_snelheid = 130 # class variabele: voor alle objecten hetzelfde
    aantal = 0  # class variabele

    # Constructor
    def __init__(self,e,v):
        print("Creatie van Object Auto")
        self.setEigenaar(e)
        self.setSnelheid(v)
        Auto.aantal += 1
        print("Aantal Auto's{}".format(Auto.aantal))


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
        return "Auto van {} met een snelheid van {}".format(self.eigenaar, self.__snelheid)


a1 = Auto("Marnick",180)
a2 = Auto("Ronald",200)
a3 = Auto("Kim",100)

print(a1.info())
print(a2.info())
print(a3.info())

