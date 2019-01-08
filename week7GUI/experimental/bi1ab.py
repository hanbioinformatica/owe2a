import tkinter


class MyGUI:

    def __init__(self): # constructor
        self.main_window = tkinter.Tk()
        self.main_window.geometry ("500x500") # bepaal grootte van window
        self.main_window.title ("GUI App voor Bi1a en Bi1b")

        self.label1 = tkinter.Label(text="Hello World!")
        self.label1.pack()

        tkinter.mainloop()


my_gui = MyGUI() # instantiering van het MyGUI object

