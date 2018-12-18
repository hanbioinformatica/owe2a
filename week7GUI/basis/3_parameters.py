import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.top_frame, text='Hello World!',\
                                    bg="red",relief="sunken")
        self.label1.pack(side="top")
        self.label2 = tkinter.Label(self.bottom_frame, text='Hallo Bi1!',\
                                    relief="raised",bg="yellow",\
                                    fg="blue")
        self.label2.pack(side="top")
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

my_gui = MyGUI()




