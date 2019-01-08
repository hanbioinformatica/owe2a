import tkinter as tk
from tkinter import *

class MyGUI:

    def __init__(self): # constructor
        self.main_window = Tk()
        self.main_window.title("Mijn eerste GUI")
        self.main_window.geometry("500x500")

        self.bovenste_frame = Frame(self.main_window,
                                            width=400,
                                            height=200,
                                            background="white")
        self.bovenste_frame.pack()   # plaats frame in het window
        self.bovenste_frame.pack_propagate(0) # voorkom verkleinen bij plaatsen van een grafisch element

        self.onderste_frame = Frame(self.main_window,
                                            width=500,
                                            height=300,
                                            background="#a34834")
        self.onderste_frame.pack()
        self.onderste_frame.pack_propagate(0)

        self.label1 = Label(self.bovenste_frame,
                                    text="Hello World!",
                                    bg="yellow",
                                    fg="blue")
        self.label1.pack()
        self.label2 = Label(self.onderste_frame,
                                    text="Hello World! Twee")
        self.label2.pack()

        self.file_open_button = Button(self.bovenste_frame,
                                               text="Open bestand",
                                               command=self.open_bestand)
        self.textarea = Text(self.onderste_frame,
                                     height=20,
                                     width=60,
                                     bg="yellow")
        self.textarea.pack()
        self.file_open_button.pack()


        mainloop()

    def open_bestand(self):

        self.file_name = tk.filedialog.askopenfilename(initialdir="~",
                                                    title="Kies een fasta bestand",
                                                    filetypes=(("All files","*.*"),("Fasta files","*.fasta")))
        print (self.file_name)
        bestand = open (self.file_name,"r")
        for regel in bestand:
            print (regel)
            self.textarea.insert(END,regel)
        bestand.close()

my_gui = MyGUI() # instantiering van het MyGUI object