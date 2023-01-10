

def number_tracker(df, col1, col2, col3):

    from variables import keno_combinations, list_conversion
    import pandas as pd
    import numpy as np
    import datetime


    df["draw_date"] = pd.to_datetime(df[col1])

    draw_dates = df["draw_date"].values

    d = pd.DataFrame(np.zeros((len(keno_combinations) + 1, len(draw_dates))))
    d.columns = draw_dates

    for c in range(len(df)):
        num_list = list_conversion(df.iloc[c][col2])
        #num_list = df.iloc[c]["Numbers_2"]
        for num in num_list:
            d.iloc[num, c] = 1

    time_of_day = df[col3].values
    dates = list(d.columns)

    for e, t in enumerate(time_of_day):
        if t == 'Evening':
            time_change = datetime.timedelta(hours=22.5)
            new_date_time = dates[e] + time_change
            new_date_time2 = datetime.datetime.strptime(str(new_date_time), "%Y-%m-%d %H:%M:%S").strftime(
                "%y-%b %#d %H:%M")

            dates[e] = new_date_time2
        else:
            time_change = datetime.timedelta(hours=14)
            new_date_time = dates[e] + time_change
            new_date_time2 = datetime.datetime.strptime(str(new_date_time), "%Y-%m-%d %H:%M:%S").strftime(
                "%y-%b %#d %H:%M")

            dates[e] = new_date_time2

    d.columns = dates

    # Save the dataframe as a csv file
    d.to_csv('data/keno_numbers_draw_dates.csv',
              index=True,
              encoding='utf-8')
