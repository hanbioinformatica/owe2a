class Auto:

    def setSnelheid(self,v):
        if v > 130:
            print ("Dat mag niet {} foei! "\
                   .format(self.eigenaar))
            self.snelheid = 130
        else:
            self.snelheid = v

    def getSnelheid(self):
        return self.snelheid

    def setEigenaar(self,e):
        self.eigenaar = e

    def getEigenaar(self):
        return self.eigenaar

    def info(self):
        print ("Dit is de auto van {} met een snelheid: {}"\
               .format(self.eigenaar,self.snelheid))






a1 = Auto()
a2 = Auto()
a3 = Auto()
a4 = Auto()
a5 = Auto()

a1.setEigenaar("Steffen")
a1.setSnelheid(70)

a2.setEigenaar("Armin")
a2.setSnelheid(100)

a3.setEigenaar("Alexander")
a3.setSnelheid(5)

a4.setEigenaar("Stijn")
a4.setSnelheid(3)

a5.setEigenaar("Rutger")
a5.setSnelheid(343)

a1.info()
a2.info()
a3.info()
a4.info()
a5.info()