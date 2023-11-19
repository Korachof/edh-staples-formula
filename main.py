from tkinter import *

window = Tk()
window.title("EDH Staple Compiler")

window.geometry('1280x720')

# canvas = Canvas(window, width= 1000, height= 750, bg="#B2C248")
# canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
# canvas.pack()

# "Please select which colors are included in your deck below"

white_button = PhotoImage(file="button_images/white.png")
blue_button = PhotoImage(file="button_images/blue.png")
black_button = PhotoImage(file="button_images/black.png")
red_button = PhotoImage(file="button_images/red.png")
green_button = PhotoImage(file="button_images/green.png")
start_button = PhotoImage(file="button_images/start_button.png")

# Configure the row and 5 columns for the buttons. 
Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.columnconfigure(window,0,weight=1)
Grid.columnconfigure(window,1,weight=1)
Grid.columnconfigure(window,2,weight=1)
Grid.columnconfigure(window,3,weight=1)
Grid.columnconfigure(window,4,weight=1)

# check button variables

white_var = 0
blue_var = 0
black_var = 0
red_var = 0
green_var = 0

# Set the MTG color buttons
white = Button(window,
                 image=white_button,
                 command=lambda: colorChoice("w"))
blue = Button(window,
                 image=blue_button,
                 command=lambda: colorChoice("u"))
black = Button(window,
                 image=black_button,
                 command=lambda: colorChoice("b"))
red = Button(window,
                 image=red_button,
                 command=lambda: colorChoice("r"))
green = Button(window,
                 image=green_button,
                 command=lambda: colorChoice("g"))

start = Button(window,
                 image=start_button)

def colorChoice(choice):
    global white_var
    global blue_var
    global black_var
    global red_var
    global green_var
    
    if choice == "w":
        if white_var == 0:
            white_var += 1
            white.config(relief=SUNKEN)
            
        else:
            white_var -= 1
            white.config(relief=RAISED)
    
    elif choice == "u":
        if blue_var == 0:
            blue_var += 1
            blue.config(relief=SUNKEN)
            
        else:
            blue_var -= 1
            blue.config(relief=RAISED)
            
    elif choice == "b":
        if black_var == 0:
            black_var += 1
            black.config(relief=SUNKEN)
            
        else:
            black_var -= 1
            black.config(relief=RAISED)
            
    elif choice == "r":
        if red_var == 0:
            red_var += 1
            red.config(relief=SUNKEN)
            
        else:
            red_var -= 1
            red.config(relief=RAISED)
           
    elif choice == "g":
        if green_var == 0:
            green_var += 1
            green.config(relief=SUNKEN)
            
        else:
            green_var -= 1
            green.config(relief=RAISED)
    

# Set the grid for each of the MTG color buttons
white.grid(row=0,
             column=0)
blue.grid(row=0,
             column=1)
black.grid(row=0,
             column=2)
red.grid(row=0,
             column=3)
green.grid(row=0,
             column=4)
start.grid(row=1,
           column=2)

window.mainloop()