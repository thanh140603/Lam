from geopy.geocoders import Nominatim
import json
import requests

geolocator = Nominatim(user_agent="my_custom_user_agent")
API_URL = "https://provinces.open-api.vn/api/?depth=1"

def get_provinces_list():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            provinces = [province["name"] for province in data]
            return provinces
        else:
            print(f"Error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Catch error: {e}")
        return []

def get_coordinates(city_name):
    location = geolocator.geocode(city_name + ", Vietnam")
    if location:
        return {"latitude": location.latitude, "longitude": location.longitude}
    else:
        return {"error": f"Not found {city_name}."}

provinces = get_provinces_list()
coordinates_list = []
for province in provinces:
    coordinates = get_coordinates(province)
    coordinates_list.append({"name": province, "coordinates": coordinates})

json_string = json.dumps(coordinates_list, ensure_ascii=False, indent=4)

print(json_string)
