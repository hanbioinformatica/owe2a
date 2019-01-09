"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Creatie d.d. 8 januari 2019
"""

import tkinter as tk
from tkinter import filedialog #speciaal voor filedialog een import


class MyGUI:

    def __init__(self): # constructor
        self.main_window = tk.Tk()
        self.main_window.geometry ("500x700") # bepaal grootte van window
        self.main_window.title ("GUI App voor Bi1a en Bi1b")

        self.bovenste_frame = tk.Frame(self.main_window,
                                            background="darkgray",  # zet de achtergrondkleur van het frame
                                            width=400,              # breedte
                                            height=200,             # hoogte van het frame
                                            borderwidth=2)          # frame kun je ook opmaak meegeven

        self.onderste_frame = tk.Frame(self.main_window,
                                          background="#c0001c",     # zet de achtergrondkleur van het frame
                                          width=400,                # in dit geval een hexadecimale codering
                                          height=200)               # kan ook met de naam van een kleur (zie hier onder)

        self.bovenste_frame.pack()                                  # plaats het frame op je window
        self.bovenste_frame.pack_propagate(0)
        self.onderste_frame.pack()

        # plaats een label (tekst)
        self.label1 = tk.Label(self.bovenste_frame,            # plaats het in een frame
                                    text="Hello World!",            # bepaal de tekst
                                    bg="yellow",                    # geef de background (bg) kleur mee
                                    fg="blue")                      # geef de forground (fg) kleur mee
        self.label1.pack()                                          # plaats het in een je frame op een positie
        self.my_button = tk.Button(self.bovenste_frame,
                                   text="Open bestand",
                                   command=self.open_bestand)
        self.my_button.pack()

        self.scrollbar = tk.Scrollbar(self.onderste_frame) # (1) maak een scrollbar object
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # (2) pack de scrollbar en plaats hem rechts

        self.tekstveld = tk.Text(self.onderste_frame,
                                 height=20,
                                 width=60,
                                 bg="#c0c0c0",
                                 yscrollcommand=self.scrollbar.set) # (3) plaats scrollbar in tekstveld
        self.scrollbar.config (command=self.tekstveld.yview) # (4) configuur gedrag
        self.tekstveld.pack()


        tk.mainloop()

    def open_bestand(self):
        self.file_name = filedialog.askopenfilename(initialdir="~"
                                                    ,title="Kies een fasta file"
                                                    ,filetypes=(("Fasta files","*.fa*"),("Alle bestanden","*.*")))
        print(self.file_name)
        bestand = open (self.file_name)
        for regel in bestand:
            self.tekstveld.insert(tk.END, regel)
        bestand.close()


onzin = MyGUI() # instantiering van het MyGUI object

