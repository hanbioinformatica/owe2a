"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Een eerste aanzet tot het bouwen van een GUI
Creatie d.d. 27 december 2018
"""

import tkinter

class MyGUI:

    def __init__(self): # constructor
        self.main_window = tkinter.Tk()
        self.main_window.title("Hello World")
        self.main_window.geometry("500x500")
        self.label = tkinter.Label(self.main_window,text="Hello World")
        self.label.pack()
        tkinter.mainloop()


my_gui = MyGUI()
