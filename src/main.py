import folium as f
import pandas as pd
import os.path

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

print(parse_addresses(pantry_data))
