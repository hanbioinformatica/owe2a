import tkinter
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',
                                        command=self.doe_iets)
        self.my_button.pack()

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.frame,
                                       text='Keuze 1', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.frame,
                                       text='Keuze 2', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.frame,
                                       text='Keuze 3', variable=self.cb_var3)
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.frame.pack()
        tkinter.mainloop()

    def doe_iets(self):
        self.message = "Keuzes:\n"
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'
        tkinter.messagebox.showinfo('response', self.message)


my_gui = MyGUI()



