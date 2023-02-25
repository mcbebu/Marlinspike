import isSimilarAddress
from GIS import get_location
from geopy.geocoders import Nominatim

# Initialize Nominatim API


temp_data = {
    "addresses": ["adr1", "adr2", "adr3", "adr4"],
    "longitude": ["1.05", "2.07", "3.62", "4.19"],
    "latitude": ["1.57", "3.76", "2.46", "4.76"],
    "description": ["desc1", "desc2", "desc3", "desc4"]
}


def prelim_lat_long(address):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude


def input_address():
    dest = input("Input the destination.")
    return dest


def location_outputs(loc_list, all_list, original_address):
    original_coords = prelim_lat_long(original_address)
    closest_locs = {
        "latitude": [],
        "longitude": [],
        "description": []
    }
    temp_all = all_list
    for adr in loc_list:
        data_pos = temp_all["address"].index(adr)
        closest_locs["latitude"].append(temp_all["latitude"].pop([data_pos]))
        closest_locs["longitude"].append(temp_all["longitude"].pop([data_pos]))
        closest_locs["description"].append(temp_all["description"].pop([data_pos]))
        temp_all.pop([data_pos])

    return original_coords, closest_locs


def new_data(all_list, new_adr, new_discr):
    all_list["address"].append(new_adr)
    lat, long = get_location()
    all_list["latitude"].append(lat)
    all_list["longitude"].append(long)
    all_list.append(new_discr)
