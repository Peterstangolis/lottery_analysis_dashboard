
from variables import data_url


## A function that returns the next draw date and time along with Midday vs Evening draw
def upcoming_draw_date(df):

    import pandas as pd
    import datetime as dt

    last_draw_date = df.tail(1)["Draw Date"].values[0]
    month = pd.DatetimeIndex(df.tail(1)["Draw Date"]).month[0]
    year = pd.DatetimeIndex(df.tail(1)["Draw Date"]).year[0]
    day = pd.DatetimeIndex(df.tail(1)["Draw Date"]).day[0]

    midd_even = df.tail(1)["Time of day"].values[0]
    # print(midd_even, last_draw_date)

    if midd_even == "Evening":
        next_draw_time = "Midday"
        next_draw_date_time = dt.datetime(year, month, day + 1, 14, 00, 00)
        return next_draw_date_time, next_draw_time
    else:
        next_draw_time = "Evening"
        next_draw_date_time = dt.datetime(year, month, day, 22, 30, 00)
        return next_draw_date_time, next_draw_time


def time_until_next_draw(df):

    import datetime as dt
    import pandas as pd

    upcoming_draw, midday_or_evening = upcoming_draw_date(df)
    # print(upcoming_draw, midday_or_evening)

    time_until_keno_draw = upcoming_draw - dt.datetime.now()

    seconds_to_draw = str(time_until_keno_draw).split(".")[0].split(":")[2]
    minutes_to_draw = str(time_until_keno_draw).split(".")[0].split(":")[1]
    hours_to_draw = str(time_until_keno_draw).split(".")[0].split(":")[0]

    next_draw_date = f"{upcoming_draw.strftime('%A')} | {upcoming_draw.strftime('%#d %b %Y')} | {midday_or_evening}"
    countdown_to_draw = f"{hours_to_draw}h : {minutes_to_draw}m :{seconds_to_draw}"

    return next_draw_date, countdown_to_draw