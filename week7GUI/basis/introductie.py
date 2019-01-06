import tkinter

class MyGUI:

    def __init__(self): # constructor
        self.main_window = tkinter.Tk()
        self.main_window.title("Hello World")
        self.main_window.geometry("500x500")
        self.label = tkinter.Label(self.main_window,text="Hello World")
        self.label.pack()
        tkinter.mainloop()


my_gui = MyGUI()
