"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Creatie d.d. 27 december 2018

"""

from tkinter import filedialog, Scrollbar
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',
                                        command=self.open_bestand)
        self.my_button.pack()
        self.frame.pack()
        tkinter.mainloop()

    def open_bestand(self):

        self.main_window.filename = filedialog.askopenfilename(initialdir="/",
                                                               title="Select file",
                                                               filetypes=(("All files", "*.*"),
                                                                          ("Fasta files", "*.fasta")))




my_gui = MyGUI()




