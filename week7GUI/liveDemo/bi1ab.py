"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Creatie d.d. 8 januari 2019
"""

import tkinter


class MyGUI:

    def __init__(self): # constructor
        self.main_window = tkinter.Tk()
        self.main_window.geometry ("500x500") # bepaal grootte van window
        self.main_window.title ("GUI App voor Bi1a en Bi1b")
        self.bg = "white"




        self.bovenste_frame = tkinter.Frame(self.main_window,
                                            background="darkgray",  # zet de achtergrondkleur van het frame
                                            width=200,              # in dit geval een hexadecimale codering
                                            height=200,             # kan ook met de naam van een kleur (zie hier onder)
                                            borderwidth=2)

        self.onderste_frame = tkinter.Frame(self.main_window,
                                          background="#c0001c",     # zet de achtergrondkleur van het frame
                                          width=200,                # in dit geval een hexadecimale codering
                                          height=200)               # kan ook met de naam van een kleur (zie hier onder)

        self.bovenste_frame.pack()                                  # plaats het frame op je window
        self.bovenste_frame.pack_propagate(0)                       # voorkom dat het frame zich aanpast aan de grootte
                                                                    # van je objecten
        self.onderste_frame.pack()

        # plaats een label (tekst)
        self.label1 = tkinter.Label(self.bovenste_frame,            # plaats het in een frame
                                    text="Hello World!",            # bepaal de tekst
                                    bg="yellow",                    # geef de background (bg) kleur mee
                                    fg="blue")                      # geef de forground (fg) kleur mee
        self.label1.pack()                                          # plaats het in een je frame op een positie



        tkinter.mainloop()


my_gui = MyGUI() # instantiering van het MyGUI object

