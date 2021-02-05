import requests
import json
from pprint import pprint
url = 'http://pro.openweathermap.org/data/2.5/forecast/hourly'
parametr = {
    'q': 'London',
    'appid': '493a14bdcf21b497b383ede86e1101ba'
}
data = requests.get(url, params=parametr).json()
pprint(data)
