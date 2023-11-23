import tkinter as tk
from tkinter import ttk
from tkinter import *


# class UI(tk.Tk):
#     def __init__(self, *args, **kwargs):
#         tk.Tk.__init__(self, *args, **kwargs)
#         self.ui_frames = {}
#         self.wm_title("MTG Staple Compiler")
        
#         ui_frame = tk.Frame(
#             self, 
#             width = 1280, 
#             height = 720
#         )
        
#         ui_frame.pack(side = "top", fill = "both", expand = True)
        
#         # make a list of ui windows to swap between 

#         ui_windows = (StartPage, MakeAccountPage, EditAccountPage, ColorSelectPage, ResultsPage, DownloadPage)
    
#         for window in ui_windows: 
#             frame = window(ui_frame, self)
            

class StartPage(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("MTG Staple Compiler")
        self.geometry("1280x720")
        
        # Configure the row and 5 columns for the buttons. 
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)
        Grid.columnconfigure(self,4,weight=1)
        
        self.welcome_label = ttk.Label(self, text="Welcome to the MTG Staple Compiler")
        self.choose_label = ttk.Label(self, text="Please choose from the options below")
        
        # configure buttons
        

        self.welcome_label.grid(row=0, column=0, padx=1, pady=1)
        self.choose_label.grid(row=1, column=0, padx=1, pady=1)
        

    

class MakeAccountPage:
    pass

class EditAccountPage:
    pass

class ColorSelectPage:
    pass

class ResultsPage:
    pass

class DownloadPage:
    pass



if __name__ == "__main__":
    testObj = StartPage()
    testObj.mainloop()