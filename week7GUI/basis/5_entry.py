import tkinter
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Invoer van een getal")
        self.main_window.geometry("500x500")
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',
                                        command=self.doe_iets)
        self.my_button.pack()
        self.invoer = tkinter.Entry (self.main_window,width=10)
        self.invoer.pack()
        self.frame.pack()
        tkinter.mainloop()

    def doe_iets(self):
        tekst = self.invoer.get()
        uitkomst = 0
        tkinter.messagebox.
        try:
            uitkomst = int(tekst)*7
        except ValueError:
            tkinter.messagebox.showwarning('Errro', 'Je moet een getal invullen')
        tkinter.messagebox.showinfo('response','Zeven keer '+tekst+' is '+str(uitkomst))

my_gui = MyGUI()



