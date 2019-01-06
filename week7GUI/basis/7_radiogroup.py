import tkinter
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',
                                        command=self.doe_iets)
        self.my_button.pack()
        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.frame,
                                       text='Keuze 1', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.frame,
                                       text='Keuze 2', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.frame,
                                       text='Keuze 3', variable=self.radio_var, value=3)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.frame.pack()
        tkinter.mainloop()

    def doe_iets(self):
        tekst = str(self.radio_var.get())
        tkinter.messagebox.showinfo('response', 'Invoer is ' + tekst)


my_gui = MyGUI()
