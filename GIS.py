import pandas as pd
import os
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions

api_key = 'AIzaSyBKLCe5ynMhpk5lYN8thXT-iT889X5L1Cs'

gmoptions = GMapOptions(
    lat=46.2437,
    lng=6.0251,
    map_type='roadmap',
    zoom=10,
)

p = gmap(
    api_key,
    gmoptions,
    title="COOL",
    width=500,
    height=400)
show(p)