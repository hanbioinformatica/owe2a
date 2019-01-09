import tkinter as tk
from tkinter import filedialog

class MyGUI:

    def __init__(self): # constructor
        self.main_window = tk.Tk()
        self.main_window.title("Mijn eerste GUI")
        self.main_window.geometry("500x500")

        self.bovenste_frame = tk.Frame(self.main_window,
                                            width=400,
                                            height=200,
                                            background="white")
        self.bovenste_frame.pack()              # plaats frame in het window
        self.bovenste_frame.pack_propagate(0)   # voorkom verkleinen bij plaatsen van een grafisch element

        self.onderste_frame = tk.Frame(self.main_window,
                                            width=500,
                                            height=300,
                                            background="#a34834")
        self.onderste_frame.pack()
        self.onderste_frame.pack_propagate(0)

        self.label1 = tk.Label(self.bovenste_frame,
                                    text="Hello World!",
                                    bg="yellow",
                                    fg="blue")
        self.label1.pack()
        self.label2 = tk.Label(self.onderste_frame,
                                    text="Hello World! Twee")
        self.label2.pack()

        self.file_open_button = tk.Button(self.bovenste_frame,
                                               text="Open bestand",
                                               command=self.open_bestand)

        self.scrollbar = tk.Scrollbar(self.onderste_frame)  # (1) Maak een scrollbar object
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # (2) Plaatsing van de scrollbar

        self.textarea = tk.Text(self.onderste_frame,
                                     height=20,
                                     width=60,
                                     bg="yellow",
                             yscrollcommand=self.scrollbar.set) # (3) plaats scrollbar in textarea
        self.scrollbar.config(command=self.textarea.yview) # (4) configuur scrollbar gedrag
        self.textarea.pack()
        self.file_open_button.pack()






        tk.mainloop()

    def open_bestand(self):

        self.file_name = tk.filedialog.askopenfilename(initialdir="~",
                                                    title="Kies een fasta bestand",
                                                    filetypes=(("All files","*.*"),("Fasta files","*.fasta")))
        print (self.file_name)
        bestand = open (self.file_name,"r")
        for regel in bestand:
            self.textarea.insert(tk.END,regel)
        bestand.close()

my_gui = MyGUI() # instantiering van het MyGUI object