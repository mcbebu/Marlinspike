import isSimilarAddress
from GIS import get_location
from geopy.geocoders import Nominatim
import AppUI
# Initialize Nominatim API


temp_data = {
    "address": ["Simpang Bedok", "Changi Airport", "Geylang Road", "Jurong East"],
    "longitude": ["103.945922", "103.989441", "103.8667", "103.741247"],
    "latitude": ["1.332934", "1.359167", "1.3000", "1.338296"],
    "description": ["Hungry", "Traveller", "Thirsty", "Worky"]
}


# print(isSimilarAddress.get_similar_addresses("adr1",2,temp_data,0))
def prelim_lat_long(address):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(address)
    if location is None:
        return 0, 0
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
        closest_locs["latitude"].append(temp_all["latitude"].pop(data_pos))
        closest_locs["longitude"].append(temp_all["longitude"].pop(data_pos))
        closest_locs["description"].append(temp_all["description"].pop(data_pos))
        temp_all["address"].pop(data_pos)

    return original_coords, closest_locs
# output is ( (coordinates), {similar address dictionary} )

# print(location_outputs(isSimilarAddress.get_similar_addresses("adr1",2,temp_data,0), temp_data, "adr1"))

def new_data(all_list, new_adr, new_discr):
    all_list["address"].append(new_adr)
    lat, long = get_location()
    all_list["latitude"].append(lat)
    all_list["longitude"].append(long)
    all_list["description"].append(new_discr)

order_address = input_address()
narrowed_list = isSimilarAddress.get_similar_addresses(order_address,2,temp_data,0)
address_n_adjacent = location_outputs(narrowed_list, temp_data, order_address)
print(address_n_adjacent[0])
print(address_n_adjacent[1])
new_description = AppUI.app(location=address_n_adjacent[0], similar=address_n_adjacent[1])
new_data(temp_data, order_address, new_description)
