import datetime


def time_to_float(dt: datetime.datetime):
    """Returns the time as a ratio
    6:30 => 6.5
    18:45 => 18.75
    """

    time = dt.time()
    return time.hour + time.minute / 60


def format_time(dt: datetime.datetime):
    """Returns a nicely formatted string showing the time"""

    return dt.strftime("%H:%M")
