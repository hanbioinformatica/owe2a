"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Creatie d.d. 27 december 2018
"""

import tkinter
# "ttk", is een verwijzing naar nieuwe "themed" widgets
from tkinter import ttk


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x500")
        self.combo = ttk.Combobox(self.main_window)
        self.combo['values'] = (1, 2, 3, 4, 5, "Text")
        self.combo.current(1)  # set the selected item
        self.combo.pack()
        tkinter.mainloop()

my_gui = MyGUI()
