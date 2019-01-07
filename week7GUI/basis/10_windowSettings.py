"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Creatie d.d. 27 december 2018
"""

import tkinter


class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        # bepaal de grootte van je window
        self.main_window.geometry("400x200")
        # geef het een titel mee
        self.main_window.title("Hello World App")
        # maak verschillende frames aan met eigen eigenschappen
        # frames zijn containers in je main_window
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        # plaats een label (tekst)
        self.label1 = tkinter.Label(self.top_frame,      # plaats het in een frame
                                    text="Hello World!", # bepaal de tekst
                                    bg="yellow",         # geef de background (bg) kleur mee
                                    fg="blue")           # geef de forground (fg) kleur mee
        self.label1.pack(side="top")                     # plaats het in een je frame op een positie

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()


my_gui = MyGUI()


