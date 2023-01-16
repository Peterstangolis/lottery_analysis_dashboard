

def groupings_to_csv(df):
    import datetime
    import pandas as pd
    import numpy as np

    url_analysis = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_analysis.csv?raw=true'

    df4 = pd.read_csv(url_analysis,
                      index_col=0)


    df4["draw_date"] = pd.to_datetime(df4["Draw Date"])


    draw_dates = df4["draw_date"].values

    d_groups = pd.DataFrame(np.zeros((8, len(draw_dates))))


    d_groups.columns = draw_dates
    d_groups


    for c in range(len(df4)):
        groups_list = df4.iloc[c]["Number Groupings"]
        groups_list_2 = groups_list.replace("{" ,"").replace("}" ,"").split(",")
        for e, i in enumerate(groups_list_2):
            list_3 = i.split(":")
            n = int(list_3[1].strip())
            d_groups.iloc[e, c] = n


    d_groups = d_groups.T


    time_of_day = df4["Time of day"].values
    dates = list(d_groups.index)


    for e ,t in enumerate(time_of_day):
        if t == 'Evening':
            time_change = datetime.timedelta(hours=22.5)
            new_date_time = dates[e] + time_change
            new_date_time2 = datetime.datetime.strptime(str(new_date_time), "%Y-%m-%d %H:%M:%S").strftime("%y-%b %#d %H:%M")
            dates[e] = new_date_time2
        else:
            time_change = datetime.timedelta(hours=14)
            new_date_time = dates[e] + time_change
            new_date_time2 = datetime.datetime.strptime(str(new_date_time), "%Y-%m-%d %H:%M:%S").strftime("%y-%b %#d %H:%M")
            dates[e] = new_date_time2


    d_groups["New_Index"] = dates
    d_groups.set_index("New_Index", inplace=True, drop=True)


    ## Save the dataframe as a csv file
    d_groups.to_csv("data/groupings_breakdown.csv",
                    index=True,
                    encoding='utf-8')