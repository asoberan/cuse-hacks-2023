from urllib import parse
import folium as f
import pandas as pd
import requests
import os.path
import pprint

DATASETS_PATH = "datasets/"

pantry_data = pd.read_csv(os.path.join(DATASETS_PATH, "OnCo_Food_Pantries_2015.csv"),
                          encoding = 'unicode_escape',
                          engine = 'python')

def parse_addresses(pantry_data):
    street = pantry_data["Street"].values.tolist()
    city = pantry_data["City"].values.tolist()
    zipcode = pantry_data["Zip"].values.tolist()

    addresses = map(lambda s, c, z: [s, c, z], street, city, zipcode)          

    return list(addresses)

def geocode(address):
    street, city, zipcode = address
    nominatim_uri = "https://nominatim.openstreetmap.org/search"
    query = {
        "street": street,
        "city": city,
        "postalcode": zipcode,
        "format": "json"
    };
    coords = requests.get(nominatim_uri, params=query)
    coords_json = coords.json()
    lat, lon = coords_json[0]["lat"], coords_json[0]["lon"]
    return lat, lon 

sample_address = parse_addresses(pantry_data)[1]
print(geocode(sample_address))
