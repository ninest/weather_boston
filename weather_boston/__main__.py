from weather_boston.charts.sun import generate_sunrise_sunset_chart
from weather_boston.file import write_files
from .temperature import temperature_display
from .settings import API_KEY
from .open_weather_map import OpenWeatherMap
from .generate_readme import README


lat = 42.3474595
lon = -71.0854323

client = OpenWeatherMap(lat=lat, lon=lon, api_key=API_KEY)
weather = client.get_weather()

# Create graphs
generate_sunrise_sunset_chart(
    sunrise=weather.sunrise,
    sunset=weather.sunset,
    current=weather.generation_time,
)


readme = README(generation_time=weather.generation_time, weather=weather)

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
