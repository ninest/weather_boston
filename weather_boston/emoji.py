def weather_emoji(description: str):
    """Return an emoji based on the description"""

    emoji_map = {
        "cloud": "☁️",
        "rain": "🌧",
        "sun": "☀️",
        "snow": "❄️",
    }

    emojis = ""
    for key in emoji_map:
        print(key,description)
        if key in description:
            emojis += emoji_map[key]
    return emojis
