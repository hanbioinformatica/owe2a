import tkinter


class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        # bepaal de grootte van je window
        self.main_window.geometry("400x200")
        # geef het een titel mee
        self.main_window.title("Hello World App")
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label1 = tkinter.Label(self.top_frame,
                                    text="Hello World!",
                                    bg="red",
                                    relief="sunken")
        self.label1.pack(side="top")

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()


my_gui = MyGUI()


