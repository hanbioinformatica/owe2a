import tkinter
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Hello World!')
        self.label.pack()
        self.my_button = tkinter.Button(self.main_window, text='klik hier niet op!',
                                        command=self.doe_iets)
        self.my_button.pack()
        tkinter.mainloop()

    def doe_iets(self):
        for i in range(10):
            tkinter.messagebox.showwarning('response','Bedankt voor het klikken!')


my_gui = MyGUI()



