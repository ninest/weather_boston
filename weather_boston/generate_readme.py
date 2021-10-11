import datetime
import humanize
from weather_boston.emoji import weather_emoji
from weather_boston.open_weather_map import WeatherData
from .temperature import kelvin_to_celcius, temperature_display


class README:
    def __init__(self, generation_time, weather: WeatherData):
        self.generation_time = generation_time
        self.weather = weather
        self.temperature_unit = "K"

    def set_temperature_unit(self, unit):
        self.temperature_unit = unit
        return self

    def generate(self):
        display_time = self.generation_time.strftime("%H:%M")

        emojis = weather_emoji(self.weather.description)
        description = self.weather.description.capitalize()
        if emojis:
            description = f"{emojis} {description}"

        temperature = temperature_display(
            self.temperature_unit, self.weather.temperature
        )
        temperature_min = temperature_display(
            self.temperature_unit, self.weather.temperature_min
        )
        temperature_max = temperature_display(
            self.temperature_unit, self.weather.temperature_max
        )
        temperature_feels_like = temperature_display(
            self.temperature_unit, self.weather.temperature_feels_like
        )

        sunrise_natural_time = humanize.naturaltime(
            datetime.datetime.now() - self.weather.sunrise
        )

        sunset_natural_time = humanize.naturaltime(
            datetime.datetime.now() - self.weather.sunset
        )

        return f"""Boston Weather, last updated {display_time}.

# {description}, {temperature}

Feels like {temperature_feels_like}

|  | Temperature |
| -- | -- |
| High | {temperature_max} |
| Low | {temperature_min} |

## Sun

Sunrise {sunrise_natural_time} and sunset {sunset_natural_time}.

![Sunrise sunset chart](./assets/sun.png)

## Build setup

Install [pyenv](https://github.com/pyenv/pyenv), then clone or fork the repository. Run


```shell
pyenv virtualenv 3.9.5 weather-boston-venv-venv

pyenv activate
pip install -r requirements.txt
```

To generate the README, run

```shell
python -m weather_boston
```
"""
