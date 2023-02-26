import isSimilarAddress
from GIS import get_location
from geopy.geocoders import Nominatim
from AppUI import app
from csv import reader, writer
from copy import deepcopy as dc

temp_data = {}

with open('data.txt', 'r', newline='') as f:
    values = [row for row in reader(f)]
    temp_data["address"] = values[0]
    temp_data["longitude"] = values[1]
    temp_data["latitude"] = values[2]
    temp_data["description"] = values[3]


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
    temp_all = dc(all_list)
    temp_all["address"] = temp_all['address'][::-1]
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
    incase = {
        "address": ["Bukit Batok St 23", "Changi Airport", "Geylang Road", "Jurong East"],
        "longitude": ["103.75587", "103.989441", "103.8667", "103.741247"],
        "latitude": ["1.34082", "1.359167", "1.3000", "1.338296"],
        "description": ["Hungry", "Traveller", "Thirsty", "Worky"]
    }
    all_list["address"].append(new_adr)
    lat, long = get_location()
    all_list["latitude"].append(lat)
    all_list["longitude"].append(long)
    all_list["description"].append(new_discr)
    with open('data.txt', 'w', newline='') as f:
        w = writer(f)
        [w.writerow(all_list[keys]) for keys in all_list.keys()]


order_address = input_address()
narrowed_list = isSimilarAddress.get_similar_addresses(order_address, 2, temp_data, 0)
# print(narrowed_list)
address_n_adjacent = location_outputs(narrowed_list, temp_data, order_address)
# print(address_n_adjacent[0])
address_n_adjacent[1]['latitude'] = [float(x) for x in address_n_adjacent[1]['latitude']]
address_n_adjacent[1]['longitude'] = [float(x) for x in address_n_adjacent[1]['longitude']]
# print(address_n_adjacent[1])
new_description = app(location=address_n_adjacent[0], similar=address_n_adjacent[1])
new_data(temp_data, order_address, new_description)
