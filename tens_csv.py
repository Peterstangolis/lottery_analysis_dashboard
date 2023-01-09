

def tens_csv(df):

    import pandas as pd
    import numpy as np
    import datetime
    from variables import keno_combinations

    df["draw_date"] = pd.to_datetime(df["Draw Date"])

    draw_dates = df["draw_date"].values
    d_zero = pd.DataFrame(np.zeros((8, len(draw_dates))))

    d_zero.columns = draw_dates


    for c in range(len(df)):
        tens_list = df.iloc[c]["Tens_Category"]
        tens_list_2 = tens_list.replace("{" ,"").replace("}" ,"").split(",")
        for e, i in enumerate(tens_list_2):
            list_3 = i.split(":")
            n = int(list_3[1].strip())
            d_zero.iloc[e, c] = n

    d_zero = d_zero.T

    time_of_day = df["Time of day"].values
    dates = list(d_zero.index)

    for e, t in enumerate(time_of_day):
        if t == 'Evening':
            time_change = datetime.timedelta(hours=22.5)
            new_date_time = dates[e] + time_change
            dates[e] = new_date_time
        else:
            time_change = datetime.timedelta(hours=14)
            new_date_time = dates[e] + time_change
            dates[e] = new_date_time

    d_zero["New_Index"] = dates
    d_zero.set_index("New_Index", inplace=True, drop=True)



    ## Save the dataframe as a csv file
    d_zero.to_csv("data/tens_breakdown.csv",
              index=True,
              encoding='utf-8')
