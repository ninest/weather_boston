from .settings import API_KEY
from .open_weather_map import OpenWeatherMap
from .generate_readme import generate_readme


lat = 42.3474595
lon = -71.0854323

client = OpenWeatherMap(lat=lat, lon=lon, api_key=API_KEY)
data = client.get_weather()
readme = generate_readme(data)

file = open("./README.md", "w")
file.write(readme)
file.close()
