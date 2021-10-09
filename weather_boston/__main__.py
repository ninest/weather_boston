from os import read

from weather_boston.file import write_files
from .temperature import temperature_display
from .settings import API_KEY
from .open_weather_map import OpenWeatherMap
from .generate_readme import README, generate_readme


lat = 42.3474595
lon = -71.0854323

client = OpenWeatherMap(lat=lat, lon=lon, api_key=API_KEY)
weather = client.get_weather()

readme = README(
    description=weather.description,
    temperature=weather.temperature,
    temperature_min=weather.temperature_max,
    temperature_max=weather.temperature_min,
    temperature_feels_like=weather.temperature_feels_like,
)

k_readme = readme.set_temperature_unit("K").generate()
c_readme = readme.set_temperature_unit("C").generate()
f_readme = readme.set_temperature_unit("F").generate()


write_files(
    [
        ["./README.md", c_readme],
        ["./F-README.md", f_readme],
        ["./K-README.md", k_readme],
    ]
)
