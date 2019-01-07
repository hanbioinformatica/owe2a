"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Creatie d.d. 27 december 2018

"""
from tkinter import filedialog, Scrollbar, END, PhotoImage, Label
import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x500")
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame1.pack()
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame2.configure(bg="red")
        self.frame2.pack()

        self.my_button = tkinter.Button(self.frame2, text='Open Image',
                                        fg = "blue", bg = "green",
                                        command=self.open_bestand)
        self.my_button.pack()
        tkinter.mainloop()


    def open_bestand(self):
        self.main_window.filename = filedialog.askopenfilename(initialdir="~",
                                                               title="Select file",
                                                               filetypes=(("Images", "*.gif"),
                                                                          ("All files", "*.*")))
        self.photo = PhotoImage(file=self.main_window.filename)
        self.label = Label(image=self.photo)
        self.label.image = self.photo
        self.label.pack()


my_gui = MyGUI()




