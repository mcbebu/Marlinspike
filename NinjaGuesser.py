from tkinter import *
from PIL import Image, ImageTk
import time

def temp_text(textbox):
    textbox.delete(0, "end")


# Create an instance of tkinter frame
win = Tk()


# Set the geometry of tkinter frame
win.geometry("360x740")

def answer_outcome():
    outcome = Label(win, fg="black", text="Your answer is x km away!", font=('Arial', 20), height=1)
    outcome.place(relx=0.5, rely=0.9, anchor=CENTER, bordermode=OUTSIDE)

# Create a canvas
game_answer_placement = Label(win, fg="black", text="Parcel Where", font=('Arial', 30), height=1)
game_answer_placement.pack()

canvas = Canvas(win, width=360, height=740)
canvas.pack()

# Load an image in the script

img = (Image.open("FrontDoor.jpg"))
print(type(img))

# Resize the Image using resize method
resized_image = img.resize((360, 350), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

# Add image to the Canvas Items
canvas.create_image(10, 10, anchor=NW, image=new_image)

game_answer_txt = Entry(win, width=50, borderwidth=2)

game_answer_txt.insert(0, "Answer here: ")
game_answer_txt.place(relx=0.5, rely=0.6, height=60, anchor=CENTER, bordermode=OUTSIDE)

game_answer_submit = Button(win, text="Submit", font=60, height=2, width=10, command=answer_outcome)

game_answer_submit.place(relx=0.5, rely=0.7, anchor=CENTER, bordermode=OUTSIDE)



win.mainloop()
