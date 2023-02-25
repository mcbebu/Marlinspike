from tkinter import *
#import GIS
from tkinterweb import HtmlFrame
import os

HTML_file_path = os.path.join(os.getcwd(), "GIS.html")
print("BREAK"+HTML_file_path)

root = Tk()
root.title("Delivery Locator")
s_width = 412
s_height = 732

root.geometry("%dx%d" % (s_width, s_height))
base_plate = Frame(root, bg="black", width=s_width, height=s_height)
base_plate.pack_propagate(0)
base_plate.pack()



def open_map_page():
    map_page = Frame(base_plate, bg="grey", width=s_width, height=s_height)
    map_page.pack_propagate(0)
    map_page.pack()
    map_frame = HtmlFrame(map_page, horizontal_scrollbar="auto")
    print("HERE")
    map_frame.load_file(HTML_file_path)

    map_frame.pack(fill="both", expand=True)

#open_map_page()

root.mainloop()
