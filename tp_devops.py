import requests
import os
from datetime import datetime as dt

cle_api = os.environ['API_KEY']
latitude = os.environ['LAT']
longitude = os.environ['LONG']


url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (latitude, longitude, cle_api)
response = requests.get(url)
data = json.loads(response.text)
print(data)

 