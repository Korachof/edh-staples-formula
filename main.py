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

button1 = Button(window,
                 image=white_button)
button1.grid(row=0, column=0)

button2 = Button(window,
                 image=blue_button)
button2.grid(row=0,
             column=1)

button3 = Button(window,
                 image=black_button)
button3.grid(row=0,
             column=2)

button4 = Button(window,
                 image=red_button)
button4.grid(row=0,
             column=3)

button5 = Button(window,
                 image=green_button)
button5.grid(row=0,
             column=4)

window.mainloop()