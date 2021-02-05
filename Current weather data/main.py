import requests
import json
from pprint import pprint
api_key = '26e020a7d39d87e718b910e1e37baf15'
city_name = 'Samarkand'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
data = requests.get(url).json()
pprint(data)
