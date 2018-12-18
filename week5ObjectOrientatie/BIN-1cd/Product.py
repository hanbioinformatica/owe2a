"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van OO aan de hand van een Auto
BIN-1c/Bin-1d
Creatie 13 december 2018:

"""

class Product:

    def __init__(self,p,n):
        self.setPrijs(p)
        self.naam = n

    def __str__(self):
        return "Productnaam {} met een prijs van {} "\
            .format(self.naam,self.prijs)

    def setPrijs(self, p):
        if (p<100):
            self.prijs = p
        else:
            print ("De prijs is te hoog!")


class Pizza(Product): # overerving uit product

    def setPrijs(self, p):
        if (p<20):
            self.prijs = p
        else:
            print ("Dit is te hoog voor een pizza!")

    def setIngr(self):
        self.lijst =[]

class Pasta(Product):
    pass


# applicatie
p1 = Pizza(9,"Fungi")
p2 = Pasta(6.65,"Spaghetti Bolognese")
p1.setPrijs(90)
p2.setPrijs(90)
print (p1)
print (p2)
