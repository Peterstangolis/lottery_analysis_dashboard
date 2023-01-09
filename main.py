


## Import the libraries
from variables import data_url
from next_draw_functions import time_until_next_draw, last_drawn_numbers, odds_and_evens, over_under_35
from tens_csv import tens_csv

import pandas as pd
import streamlit as st


# Initial page setup
st.set_page_config(page_icon= '🎲',
                   layout="wide",
                   initial_sidebar_state="expanded",
                   page_title="Lottery Number Analysis"
                   )

## Load dataset

def load_data(url):
    df = pd.read_csv(url, index_col=0)
    return df

df = load_data(data_url)

tens_csv(df)


df2 = df[['Time of day', 'Numbers_2', 'Odds_vs_Evens', 'Over_Under_35', 'Repeated Numbers', \
          'Consecutive_Numbers', 'Tens_Category', 'Sum_of_picks',
          ]]

#Numbers_2", "Odds_vs_Evens", "Repeated Numbers", "Two_Game_Number_Comparison",\
    #     'Consecutive_Numbers', "Over_Under_35", "Tens_Category", "Sum_of_picks"]]


st.metric(label="TOTAL GAMES",
          value=len(df))

col1, col2, col3 = st.columns((1,1,4), gap="medium")


with col1:
    #st.image('images/number-blocks.png', width=50)

    o_e = odds_and_evens(df, "Odds_vs_Evens")

    st.metric(label="ODD #'s",
              value=f'{o_e[0]}')
    st.metric(label="EVEN #'s",
              value=f'{o_e[1]}')

with col2:

    over_under = over_under_35(df=df, col_name="Over_Under_35")
    st.metric(label="1-34",
              value=f"{over_under[1]}"
              )
    st.metric(label="35-70",
              value=f"{over_under[0]}"
              )

with col3:
    df_tens = pd.read_csv(
        "data/tens_breakdown.csv",
        index_col=0
    )

    st.line_chart(df_tens)

with st.sidebar:
    st.image('images/ca-keno-2x-png.png', width=150)
    col6, col7, col8 = st.columns((.5, 3, .5), gap='small')
    col6 = st.write(" ")
    col7 = st.write("NEXT DRAW")
    next_draw_date_1, count_down_1, last_draw_date_1 = time_until_next_draw(df)
    st.write(next_draw_date_1, unsafe_allow_html=True)
    st.write(count_down_1, unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)
    st.write("LAST DRAW", unsafe_allow_html=True)
    st.write(last_draw_date_1)
    last_numbers = last_drawn_numbers(df=df, col_name="Numbers_2")
    st.write(last_numbers)

with st.expander(label="VIEW TABLE OF PREVIOUS DRAW STATS"):
    st.dataframe(df2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Program Running')





