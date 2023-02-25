from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions, HoverTool, ColumnDataSource
from winrt.windows.devices import geolocation
# get gps coordinates from geopy
import json

# import urlopen from urllib.request
from urllib.request import urlopen

api_key = 'AIzaSyBKLCe5ynMhpk5lYN8thXT-iT889X5L1Cs'
Exsimilar = {
    'longitude': [-6.215555671220000],
    'latitude': [106.22891070606781],
    'description': ["Additional Infomation"]}
Exlocation = (-6.215555671198995, 106.28891070606781)


def createhtml(location=Exlocation, similar=Exsimilar):
    hover = HoverTool(tooltips=[
        ('Description', '@description')
    ])
    similar['longitude'].append(location[0])
    similar['latitude'].append(location[1])
    similar['description'].append("Target Location")
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
    _ = p.cross('latitude', 'longitude', size=20, color='blue', source=source)
    show(p)


def get_location():
    # open following url to get ipaddress
    urlopen("http://ipinfo.io/json")
    # load data into array
    data = json.load(urlopen("http://ipinfo.io/json"))
    # extract latitude
    lat = data['loc'].split(',')[0]
    # extract longitude
    lon = data['loc'].split(',')[1]
    return lat, lon
