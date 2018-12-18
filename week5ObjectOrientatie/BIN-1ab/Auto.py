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



class elektrischeAuto(Auto):

    def opladen(self):
        print ("Auto laden")


class benzineAuto(Auto):

    def tanken(self):
        print ("Benzine tanken")


a1 = elektrischeAuto(90)
a1.setEigenaar("Wouter")

a2 = benzineAuto(110)
a2.setEigenaar("Melissa")

print (a1)
print (a2)
a1.opladen()
a2.tanken()

