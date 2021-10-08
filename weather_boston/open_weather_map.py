from typing import TypedDict
import requests


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
        return {
            "description": data["weather"][0]["description"],
            "temperature": {
                "current": data["main"]["temp"],
                "max": data["main"]["temp_max"],
                "min": data["main"]["temp_min"],
                "feels_like": data["main"]["feels_like"],
            },
        }

    def fetch(self):
        full_url=self.url_base + self.url
        request = requests.get(full_url)
        return request.json()
