from tkinter import filedialog
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',
                                        command=self.open_bestand)
        self.my_button.pack()
        self.invoer = tkinter.Entry (self.main_window,width=10)
        self.invoer.pack()
        self.frame.pack()
        tkinter.mainloop()

    def open_bestand(self):

        self.main_window.filename = filedialog.askopenfilename(initialdir="/",
                                                               title="Select file",
                                                               filetypes=(("All files", "*.*"),
                                                                          ("Fasta files", "*.fasta")))




my_gui = MyGUI()




