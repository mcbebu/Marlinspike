from tkinter import *


root = Tk()
root.title("Delivery Locator")
s_width = 412
s_height = 732

root.geometry("%dx%d" % (s_width, s_height))
base_plate = Frame(root, bg="black", width=s_width, height=s_height)
base_plate.pack_propagate(0)
base_plate.pack()

root.mainloop()