import datetime
from os import terminal_size
from typing import Union
import requests
from dataclasses import dataclass

from weather_boston.temperature import kelvin_to_celcius, kelvin_to_farenheit


@dataclass
class WeatherData:
    generation_time: datetime.datetime
    description: str
    temperature: float

    temperature_min: float
    temperature_max: float
    temperature_feels_like: float


class OpenWeatherMap:
    def __init__(self, lat, lon, api_key) -> None:
        self.lon = lon
        self.lat = lat

        self.api_key = api_key

        self.api_version = "2.5"
        self.url = ""
        self.url_base = f"https://api.openweathermap.org/data/{self.api_version}/"

    def get_weather(self):
        self.url = f"weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}"
        data = self.fetch()

        return WeatherData(
            generation_time=datetime.datetime.now(),
            description=data["weather"][0]["description"],
            temperature=data["main"]["temp"],
            temperature_max=data["main"]["temp_max"],
            temperature_min=data["main"]["temp_min"],
            temperature_feels_like=data["main"]["feels_like"],
        )

    def fetch(self):
        full_url = self.url_base + self.url
        request = requests.get(full_url)
        return request.json()
