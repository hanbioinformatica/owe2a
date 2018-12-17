"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van polymorfisme aan de hand van dieren
Creatie d.d. 13 december 2018

"""

class Dier:
    def __init__(self, naam):    # Constructor van de class
        self.__naam = naam

    def geluid(self):              # Methode moet per dier worden ingevuld
        pass                       # Dieren maken een geluid, maar het geluid kan
                                    # pas op subclass niveau worden ingevuld


class Kat(Dier):
    def geluid(self):
        return 'Miauw!'

class Hond(Dier):
    def geluid(self):
        return 'Woef!'


dieren = [Kat('Gelaarsde'),
          Hond('Goofy'),
          Hond('Lassie')]

for dier in dieren:
    print (dier.__naam + ': ' + dier.geluid())
