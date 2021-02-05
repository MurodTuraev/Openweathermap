import requests
import json
from pprint import pprint
url = 'https://api.openweathermap.org/data/2.5/onecall'
parametr = {
    'lat': '33.441792',
    'lon': '-94.037689',
    'exclude': 'hourly',
    'appid': '493a14bdcf21b497b383ede86e1101ba'
}

data = requests.get(url, params=parametr).json()
pprint(data)
