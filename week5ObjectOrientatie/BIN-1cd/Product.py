class Product:

    def __init__(self,p,n):
        self.prijs = p
        self.naam = n

    def __str__(self):
        return "Productnaam {} met een prijs van {} "\
            .format(self.naam,self.prijs)


class Pizza(Product): # overerving uit product

    def setIngr(self):
        self.lijst =[]

class Pasta(Product):
    pass


# applicatie
p1 = Pizza(9,"Fungi")
p2 = Pasta(6.65,"Spagetti Bolognesse")
print (p1)
print (p2)
