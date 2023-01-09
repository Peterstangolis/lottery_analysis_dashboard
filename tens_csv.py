

def tens_csv(df):

    import pandas as pd
    import numpy as np
    from variables import keno_combinations

    draw_dates = df["Draw Date"].values
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

    ## Save the dataframe as a csv file
    d_zero.to_csv("data/tens_breakdown.csv",
              index=True,
              encoding='utf-8')
