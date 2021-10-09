def temperature_display(unit, temperature):
    """Convert from K to K, C, or F in a nicely formatted string"""

    unit_conversion_map = {
        "K": lambda t: t,
        "C": kelvin_to_celcius,
        "F": kelvin_to_farenheit,
    }
    return f"{unit_conversion_map[unit](temperature)}º{unit}"


def kelvin_to_celcius(temperature):
    return round(temperature - 273.15, 1)


def kelvin_to_farenheit(temperature):
    return round(
        (temperature - 273.15) * 9 / 5 +32,
        1,
    )
