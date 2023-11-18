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

# Configure the row and 5 columns for the MTG buttons. 
Grid.rowconfigure(window,0,weight=1)
Grid.columnconfigure(window,0,weight=1)
Grid.columnconfigure(window,1,weight=1)
Grid.columnconfigure(window,2,weight=1)
Grid.columnconfigure(window,3,weight=1)
Grid.columnconfigure(window,4,weight=1)

# Set the MTG color buttons
white = Button(window,
                 image=white_button)
blue = Button(window,
                 image=blue_button)
black = Button(window,
                 image=black_button)
red = Button(window,
                 image=red_button)
green = Button(window,
                 image=green_button)

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

window.mainloop()