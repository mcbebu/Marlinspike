from tkinter import *
import pandas as pd
import pandas_bokeh
from bokeh.io import show, output_notebook
from bokeh.plotting import figure
import glob
pandas_bokeh.output_notebook()
pd.set_option('plotting.backend', 'pandas_bokeh')

root = Tk()
root.title("Delivery Locator")
s_width = 412
s_height = 732

root.geometry("%dx%d" % (s_width, s_height))
base_plate = Frame(root, bg="black", width=s_width, height=s_height)
base_plate.pack_propagate(0)
base_plate.pack()

def open_map_page:
    map_page = Frame(base_plate, bg="grey", width=s_width, height=s_height)
    map_page.pack_propagate(0)

    map_page.pack()

root.mainloop()