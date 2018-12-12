"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van OO aan de hand van een Auto
BIN-1a/Bin-1b
Creatie d.d. 12 december 2018

"""

class Auto:

    max_snelheid = 130
    aantal = 0

    """Constructor: wordt aangeroepen bij initialisatie
    van het object"""
    def __init__(self,v):
        print("Creatie van Auto met snelheid {}".format(v))
        self.setSnelheid(v)
        Auto.aantal += 1
        print ("Aantal gemaakte auto's "+str(Auto.aantal))

    def setSnelheid(self,v):
        if v > 130:
            print ("Dat mag niet!")
            self.__snelheid = Auto.max_snelheid
        else:
            self.__snelheid = v

    def getSnelheid(self):
        return self.__snelheid

    def setEigenaar(self,e):
        self.__eigenaar = e

    def getEigenaar(self):
        return self.__eigenaar

    def info(self):
        print ("Dit is de auto van {} met een snelheid: {}" \
               .format(self.__eigenaar, self.__snelheid))

    def __str__(self):
        return "Dit is een auto van "+self.__eigenaar





a1 = Auto(100)
a2 = Auto(70)
a3 = Auto(80)
a4 = Auto(55)
a5 = Auto(343)

a1.setEigenaar("Steffen")
a2.setEigenaar("Armin")
a3.setEigenaar("Alexander")
a4.setEigenaar("Stijn")
a5.setEigenaar("Rutger")

a1.info()
a2.info()
a3.info()
a4.info()
a5.info()




