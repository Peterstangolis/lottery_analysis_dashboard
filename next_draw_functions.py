
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
        last_draw_date = dt.datetime(year, month, day)
        return next_draw_date_time, next_draw_time, last_draw_date, midd_even
    else:
        next_draw_time = "Evening"
        next_draw_date_time = dt.datetime(year, month, day, 22, 30, 00)
        last_draw_date = dt.datetime(year, month, day)
        return next_draw_date_time, next_draw_time, last_draw_date, midd_even


def time_until_next_draw(df):

    import datetime as dt

    upcoming_draw, midday_or_evening, last_draw_date, midday_or_evening_last = upcoming_draw_date(df)
    # print(upcoming_draw, midday_or_evening)

    time_until_keno_draw = upcoming_draw - dt.datetime.now()

    seconds_to_draw = str(time_until_keno_draw).split(".")[0].split(":")[2]
    minutes_to_draw = str(time_until_keno_draw).split(".")[0].split(":")[1]
    hours_to_draw = str(time_until_keno_draw).split(".")[0].split(":")[0]

    next_draw_date = f"{upcoming_draw.strftime('%A')} | {upcoming_draw.strftime('%#d %b %Y')} | {midday_or_evening}"
    countdown_to_draw = f"{hours_to_draw}h : {minutes_to_draw}m :{seconds_to_draw}"

    last_draw_date_format = f"{last_draw_date.strftime('%A')} | {last_draw_date.strftime('%#d %b %Y')} | {midday_or_evening_last}"

    return next_draw_date, countdown_to_draw, last_draw_date_format

# Return the last draws numbers
def last_drawn_numbers(df, col_name):

    last_drawn_numbers = df.iloc[len(df)-1][col_name]

    return last_drawn_numbers

def odds_and_evens(df, col_name):

    odds_and_evens = df.iloc[len(df) - 1][col_name]

    split_1 = odds_and_evens.split(",")

    odds_evens_list = []
    for item in split_1:
        n = item.split(":")[1].replace("}", "")
        odds_evens_list.append(n)
    return odds_evens_list


def over_under_35(df, col_name):

    over_under = df.iloc[len(df)-1][col_name]

    split_1 = over_under.split(",")
    over_under_list = []
    for item in split_1:
        n = item.split(":")[1].replace("}", "")
        over_under_list.append(n)

    return over_under_list

