from .temperature import kelvin_to_celcius


def generate_readme(data):
    return f"""# Boston Weather

> {data["description"].capitalize()}, {kelvin_to_celcius( data["temperature"]["current"])}ºC

|  | Temperature |
| -- | -- |
| High | {kelvin_to_celcius( data["temperature"]["max"])}ºC |
| Low | {kelvin_to_celcius( data["temperature"]["min"])}ºC |


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
