import datetime
from weather_boston.emoji import weather_emoji
from weather_boston.open_weather_map import WeatherData
from .temperature import kelvin_to_celcius, temperature_display


class README:
    def __init__(
        self,
        description,
        temperature,
        temperature_min,
        temperature_max,
        temperature_feels_like,
    ):
        self.description = description
        self.temperature = temperature
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.temperature_feels_like = temperature_feels_like

        self.temperature_unit = "K"
        self.generation_time = datetime.datetime.now()

    def set_temperature_unit(self, unit):
        self.temperature_unit = unit

        return self

    def generate(self):
        display_time = self.generation_time.strftime("%H:%-M")

        emojis = weather_emoji(self.description)
        description = self.description.capitalize()
        if emojis:
            description = f"{emojis} {description}"    

        temperature = temperature_display(self.temperature_unit, self.temperature)
        temperature_min = temperature_display(
            self.temperature_unit, self.temperature_min
        )
        temperature_max = temperature_display(
            self.temperature_unit, self.temperature_max
        )
        temperature_feels_like = temperature_display(
            self.temperature_unit, self.temperature_feels_like
        )

        return f"""Boston Weather, last updated {display_time}.

# {description}, {temperature}

Feels like {temperature_feels_like}

|  | Temperature |
| -- | -- |
| High | {temperature_max} |
| Low | {temperature_min} |


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

