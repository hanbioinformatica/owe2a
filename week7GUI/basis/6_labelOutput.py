import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='klik!',
                                        command=self.doe_iets)
        self.my_button.pack()
        self.invoer = tkinter.Entry(self.main_window, width=10)
        self.invoer.pack()

        self.value = tkinter.StringVar()
        self.value_label = tkinter.Label(self.main_window,
                                         textvariable=self.value)
        self.value_label.pack()

        self.frame.pack()
        tkinter.mainloop()

    def doe_iets(self):
        tekst = self.invoer.get()
        self.value.set(tekst)


my_gui = MyGUI()



