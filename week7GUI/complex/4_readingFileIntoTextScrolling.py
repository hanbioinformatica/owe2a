"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Creatie d.d. 7 januari 2019
"""
from tkinter import filedialog, RIGHT, Scrollbar, Y, END
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame1.pack()
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame2.configure(bg="red")
        self.frame2.pack()

        self.my_button = tkinter.Button(self.frame2, text='Open bestand',
                                        fg = "blue", bg = "green",
                                        command=self.open_bestand)
        self.my_button.pack()

        self.scrollbar = Scrollbar(self.frame1)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text = tkinter.Text(self.frame1, height=20, width=60, bg="yellow", yscrollcommand = self.scrollbar.set)
        self.text.pack()
        self.scrollbar.config(command=self.text.yview)
        tkinter.mainloop()


    def open_bestand(self):
        self.main_window.filename = filedialog.askopenfilename(initialdir="~",
                                                               title="Select file",
                                                               filetypes=(("All files", "*.*"),
                                                                          ("Fasta files", "*.fasta")))
        bestand = open (self.main_window.filename,"r")
        for regel in bestand:
            self.text.insert(END, regel)
        bestand.close()


my_gui = MyGUI()




