Boston Weather, last updated 02:22 [[C](https://github.com/ninest/weather_boston/blob/main/README.md) | **K** | [F](https://github.com/ninest/weather_boston/blob/main/F-README.md)]

# ☁️ Overcast clouds, 288.89ºK

Feels like 288.84ºK

|  | Temperature |
| -- | -- |
| High | 290.22ºK |
| Low | 286.98ºK |

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
