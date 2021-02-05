import requests
import json
from pprint import pprint
url = f'http://api.openweathermap.org/data/2.5/weather'
parametr = {
    'q': 'Samarkand',
    'appid': '26e020a7d39d87e718b910e1e37baf15'
}
data = requests.get(url, params=parametr).json()
pprint(data)
