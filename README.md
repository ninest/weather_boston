Boston Weather, last updated 02:22 [**C** | [K](https://github.com/ninest/weather_boston/blob/main/K-README.md) | [F](https://github.com/ninest/weather_boston/blob/main/F-README.md)]

# ☁️ Overcast clouds, 15.7ºC

Feels like 15.7ºC

|  | Temperature |
| -- | -- |
| High | 17.1ºC |
| Low | 13.8ºC |

## Sun

Around 13 hours of sunlight. Sunrise 4 hours from now and sunset 15 hours from now.

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
