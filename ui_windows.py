import tkinter as tk
from tkinter import *
import sys

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
            

class WindowScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("MTG Staple Compiler")
        self.geometry("1280x720")
        
        Grid.rowconfigure(self,0,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        self.frame_hash = {0: StartPage, 1: ColorSelectPage, 2: ResultsPage}
        self.current_window = 0
        self.button_command = self.frame_hash[self.current_window]
        self.frame = self.create_frame(self.current_window)
        

    def create_frame(self, buttonNum):
        for widgets in self.button_command.winfo_children(self):
            widgets.destroy()
        self.current_window = buttonNum
        self.button_command = self.frame_hash[buttonNum]
        self.button_command.tkraise(self)
        
        self.frame = self.button_command(self.frame_hash, self)
        
        self.frame.grid(row=0, column=0)
   
        
class StartPage(tk.Frame):
    def __init__(self, frameHash, mainWindow):
        super().__init__()
        self.frameHash = frameHash
        self.mainWindow = mainWindow
        self.label = tk.Label(self, text="Main Page")
        # create the button images 
        self.start_button = PhotoImage(file="button_images/start_button.png")  
        
        # Configure the row and 5 columns for the buttons. 
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)
        Grid.columnconfigure(self,4,weight=1)
        
        self.welcome_label = tk.Label(self, text="Welcome to the MTG Staple Compiler")
        self.choose_label = tk.Label(self, text="Please choose from the options below")
        self.start = tk.Button(self,
                    image=self.start_button)
       

        self.options_frame = tk.Frame(self)
        self.options_frame.grid(row=3, column=2, padx=1, pady=1)
        
        self.color_choice = tk.Button(self.options_frame, 
                                      text="Choose Deck Colors", 
                                      bg="#2f9fd6",
                                      fg="white", 
                                      activebackground="#146d99", 
                                      activeforeground="white", 
                                      font="Garamond",
                                      command=lambda: self.mainWindow.create_frame(1))
        
        self.custom_list = tk.Button(self.options_frame, 
                                     text="Create Custom Staples List", 
                                     bg="#2f9fd6", 
                                     fg="white", 
                                     activebackground="#146d99", 
                                     activeforeground="white", 
                                     font="Garamond",
                                     command=lambda: self.mainWindow.create_frame(2))
        
        self.exit_button = tk.Button(self.options_frame,
                                     text="Exit",
                                     bg="#2f9fd6",
                                     fg="white", 
                                     activebackground="#146d99", 
                                     activeforeground="white",
                                     font="Garamond", 
                                     command=sys.exit)
        
        self.color_choice.grid(row=0, column=0, padx=1, pady=2, sticky="WES")
        self.custom_list.grid(row=1, column=0, padx=1, pady=2, sticky="WEN")
        self.exit_button.grid(row=2, column=0, padx=1, pady=2, sticky="WEN")
        
        # configure buttons
        
        self.welcome_label.grid(row=0, column=2, padx=1, pady=1)
        self.choose_label.grid(row=1, column=2, padx=1, pady=1)
        self.start.grid(row=2, column=2, padx=1, pady=1)
        

class MakeAccountPage:
    pass


class EditAccountPage:
    pass


class ResultsPage(tk.Frame):
    def __init__(self, frameHash, mainWindow):
        super().__init__()
        self.frameHash = frameHash
        self.mainWindow = mainWindow
        self.label = tk.Label(self, text="Color Select Page")
        # create the button images 
        self.start_button = PhotoImage(file="button_images/start_button.png")

        # Configure the row and 5 columns for the buttons. 
        # Configure the row and 5 columns for the buttons. 
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)
        Grid.columnconfigure(self,4,weight=1)

        self.select_color_label = tk.Label(self, text="Please select all the colors of your deck below")
        self.test_grid_label = tk.Label(self, text="I'm testing how this silly grid really works, dawg")
        self.exit_button = tk.Button(self,
                                     text="Exit",
                                     bg="#2f9fd6",
                                     fg="white", 
                                     activebackground="#146d99", 
                                     activeforeground="white",
                                     font="Garamond", 
                                     command=sys.exit)

        self.test_grid_label.grid(row=1, column=1)
        self.select_color_label.grid(row=2, column=2, padx=1, pady=1)
        self.exit_button.grid(row=5, column=2)


class ColorSelectPage(tk.Frame):
    def __init__(self, frameHash, mainWindow):
        super().__init__()
        self.frameHash = frameHash
        self.mainWindow = mainWindow
        self.label = tk.Label(self, text="Color Select Page 2")
        
        # text label
        self.directions_label = tk.Label(self, text="Please select each button that represents your commander's color identity below.", font="Garamond")
        self.directions_label2 = tk.Label(self, text="Once finished, select the Staples List you would like to use from the dropdown menu.", font="Garamond")
        self.directions_label3 = tk.Label(self, text="Then press Start", font="Garamond")
        
        # "Please select which colors are included in your deck below"
        self.white_button = PhotoImage(file="button_images/white.png")
        self.blue_button = PhotoImage(file="button_images/blue.png")
        self.black_button = PhotoImage(file="button_images/black.png")
        self.red_button = PhotoImage(file="button_images/red.png")
        self.green_button = PhotoImage(file="button_images/green.png")
        
        self.start_button = PhotoImage(file="button_images/start_button.png")

        # Configure the row and 5 columns for the buttons. 
        Grid.rowconfigure(self,0,weight=1)
        Grid.rowconfigure(self,1,weight=1)
        Grid.rowconfigure(self,2,weight=1)
        Grid.rowconfigure(self,3,weight=1)
        Grid.rowconfigure(self,4,weight=1)
        Grid.rowconfigure(self,5,weight=1)
        Grid.rowconfigure(self,6,weight=1)
        Grid.columnconfigure(self,0,weight=1)
        Grid.columnconfigure(self,1,weight=1)
        Grid.columnconfigure(self,2,weight=1)
        Grid.columnconfigure(self,3,weight=1)
        Grid.columnconfigure(self,4,weight=1)

        # check button variables
        self.white_var = 0
        self.blue_var = 0
        self.black_var = 0
        self.red_var = 0
        self.green_var = 0

        self.options_frame = tk.Frame(self)
        self.options_frame.grid(row=3, column=2, padx=1, pady=20, sticky="S")

        # Set the MTG color buttons
        self.white = Button(self.options_frame,
                         image=self.white_button,
                         command=lambda: self.color_choice("w"))
        self.blue = Button(self.options_frame,
                         image=self.blue_button,
                         command=lambda: self.color_choice("u"))
        self.black = Button(self.options_frame,
                         image=self.black_button,
                         command=lambda: self.color_choice("b"))
        self.red = Button(self.options_frame,
                         image=self.red_button,
                         command=lambda: self.color_choice("r"))
        self.green = Button(self.options_frame,
                         image=self.green_button,
                         command=lambda: self.color_choice("g"))
        
        # set dropdown menu
        
        self.staple_options = ["Mighty Joe Young",
                               "Cobra Kai"]
        
        self.staple_menu = StringVar(self)
        self.staple_menu.set(self.staple_options[0])

        self.staple_menu_options = OptionMenu(self, self.staple_menu, *self.staple_options)
        self.staple_menu_options.config(bg="#2f9fd6", fg="white", font="Garamond")

        self.staple_menu_options.grid(row=6, column = 2, sticky="SWE")
        
        # set menu option buttons 

        self.return_to_start_button = tk.Button(self,
                                                text="Return to the Main Menu",
                                                bg="#2f9fd6",
                                                fg="white", 
                                                activebackground="#146d99", 
                                                activeforeground="white",
                                                font="Garamond",
                                                command=lambda: self.mainWindow.create_frame(0))

        self.exit_button = tk.Button(self,
                                     text="Exit",
                                     bg="#2f9fd6",
                                     fg="white", 
                                     activebackground="#146d99", 
                                     activeforeground="white",
                                     font="Garamond", 
                                     command=sys.exit)

        self.start = Button(self,
                         image=self.start_button)
        

        # Set the grid for the instructions
        self.directions_label.grid(row=0, column=2, columnspan=5)
        self.directions_label2.grid(row=1, column=2, columnspan=5)
        self.directions_label3.grid(row=2, column=2, columnspan=5)
        
        # Set the grid for each of the MTG color buttons
        self.white.grid(row=1,
                        column=0,
                        padx=2)
        self.blue.grid(row=1,
                        column=1,
                        padx=2)
        self.black.grid(row=1,
                        column=2,
                        padx=2)
        self.red.grid(row=1,
                        column=3,
                        padx=2)
        self.green.grid(row=1,
                        column=4,
                        padx=2)
        
        # Set the grid for the Return to Main Menu button
        self.return_to_start_button.grid(row=4,
                                         column=2,
                                         sticky="SWE")

        # Set the grid for the exit button
        self.exit_button.grid(row=5,
                   column=2,
                   sticky="SWE")

    def color_choice(self, choice):
        if choice == "w":
            if self.white_var == 0:
                self.white_var += 1
                self.white.config(relief=SUNKEN, bg="grey")
            
            else:
                self.white_var -= 1
                self.white.config(relief=RAISED, bg="white")
    
        elif choice == "u":
            if self.blue_var == 0:
                self.blue_var += 1
                self.blue.config(relief=SUNKEN, bg="grey")
            
            else:
                self.blue_var -= 1
                self.blue.config(relief=RAISED, bg="white")
            
        elif choice == "b":
            if self.black_var == 0:
                self.black_var += 1
                self.black.config(relief=SUNKEN, bg="grey")
            
            else:
                self.black_var -= 1
                self.black.config(relief=RAISED, bg="white")
            
        elif choice == "r":
            if self.red_var == 0:
                self.red_var += 1
                self.red.config(relief=SUNKEN, bg="grey")
            
            else:
                self.red_var -= 1
                self.red.config(relief=RAISED, bg="white")
           
        elif choice == "g":
            if self.green_var == 0:
                self.green_var += 1
                self.green.config(relief=SUNKEN, bg="grey")
            
            else:
                self.green_var -= 1
                self.green.config(relief=RAISED, bg="white")


class DownloadPage:
    pass



if __name__ == "__main__":
    testObj = WindowScreen()
    testObj.mainloop()