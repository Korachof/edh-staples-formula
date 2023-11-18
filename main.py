from tkinter import *

window = Tk()

# "Please select which colors are included in your deck below"

white_button = PhotoImage(file="button_images/white.png")
blue_button = PhotoImage(file="button_images/blue.png")
black_button = PhotoImage(file="button_images/black.png")
red_button = PhotoImage(file="button_images/red.png")
green_button = PhotoImage(file="button_images/green.png")

button1 = Button(window,
                 image=white_button)
button1.grid()

button2 = Button(window,
                 image=blue_button)
button2.grid()

button3 = Button(window,
                 image=black_button)
button3.grid()

button4 = Button(window,
                 image=red_button)
button4.grid()

button5 = Button(window,
                 image=green_button)
button5.grid()

window.mainloop()