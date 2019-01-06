import tkinter
# "ttk", is Python's binding to the newer "themed widgets"
from tkinter import ttk


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.combo = ttk.Combobox(self.main_window)
        self.combo['values'] = (1, 2, 3, 4, 5, "Text")
        self.combo.current(1)  # set the selected item
        self.combo.pack()
        tkinter.mainloop()

my_gui = MyGUI()
