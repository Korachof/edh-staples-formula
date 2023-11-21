import tkinter as tk
from tkinter import ttk
from tkinter import *


class ui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
       
        self.wm_title("MTG Staple Compiler")
        
        ui_frame = tk.Frame(
            self, 
            width = 1280, 
            height = 720
        )
        
        ui_frame.pack(side = "top", fill = "both", expand = True)


if __name__ == "__main__":
    testObj = ui()
    testObj.mainloop()