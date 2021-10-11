import datetime
import matplotlib.pyplot as plt

from weather_boston.time import format_time, time_to_float

plt.style.use("./style/minim.mplstyle")
# plt.style.use('./style/minim-dark.mplstyle')


def generate_sunrise_sunset_chart(
    sunrise: datetime.datetime,
    sunset: datetime.datetime,
    current: datetime.datetime,
):
    """Generate a horizontal bar chart with the sunrise and sunset timings"""

    fig, ax = plt.subplots()

    # The bar should shart at sunrise and end at sunset
    # First make an orange bar for the sunset
    ax.barh([1], [time_to_float(sunset)], color="orange")
    # Then make a transparent bar for sunset
    ax.barh([1], [time_to_float(sunrise)], color="white")

    # Vertical line to show current time
    ax.axvline(x=time_to_float(current), linewidth=1, color="black", ls="--")

    # x-axis labels should be the time
    ax.set_xticks(
        [0, time_to_float(sunrise), 12, time_to_float(sunset), 24],
    )
    ax.set_xticklabels(
        ["", format_time(sunrise), "12:00", format_time(sunset), ""],
    )

    ax.set_xlim([4.0, 21.0])

    # No y-axis labels required
    ax.set_yticks([])

    plt.tight_layout()

    fig.set_size_inches(7, 3)
    fig.savefig("./assets/sun.png")


if __name__ == "__main__":
    today = datetime.datetime.now()
    sunrise = today.replace(hour=6, minute=30)
    sunset = today.replace(hour=18, minute=00)
    generate_sunrise_sunset_chart(sunrise, sunset, today.replace(hour=12, minute=50))
