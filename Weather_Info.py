import requests
#imported Requests -> a python module used to make request to the web page.
from pprint import pprint
#used prettyprints module here to get data in a formatted manner. 
# The pprint module in Python is a utility module that you can use to print data structures in a readable, pretty way. It's a part of the standard library that's especially useful for debugging code dealing with API requests, large JSON files, and data in general.

API_key = '709f913059272b40e69abcb6b840e8bd'

city = input("Enter a city: ")

base_URL = "https://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city

weather_data = requests.get(base_URL).json()

pprint(weather_data)
