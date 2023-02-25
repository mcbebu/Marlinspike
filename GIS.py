import pandas as pd
import os
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions, HoverTool, ColumnDataSource
api_key = 'AIzaSyBKLCe5ynMhpk5lYN8thXT-iT889X5L1Cs'
Exsimilar = {
    'x': [-6.215555671220000],
    'y': [106.22891070606781],
    'desc': ["Additional Infomation"]}
Exlocation = (-6.215555671198995, 106.28891070606781)

def createhtml(location=Exlocation, similar=Exsimilar):

    hover = HoverTool(tooltips=[
        ('Description', '@desc')
    ])
    similar['x'].append(location[0])
    similar['y'].append(location[1])
    similar['desc'].append("Target Location")
    source = ColumnDataSource(data=similar)
    gmoptions = GMapOptions(
        lat=location[0],
        lng=location[1],
        map_type='roadmap',
        zoom=10,
    )
    p = gmap(
        api_key,
        gmoptions,
        title="COOL",
        width=500,
        height=400,
        tools=[hover, 'reset', 'wheel_zoom', 'pan']
    )
    _ = p.cross('y', 'x', size=20, color='blue', source=source)
    show(p)

createhtml()
