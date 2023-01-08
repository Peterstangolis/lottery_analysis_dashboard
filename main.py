


## Import the libraries
from variables import data_url
from next_draw_functions import time_until_next_draw, last_drawn_numbers

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

col1, col2, col3 = st.columns((1, 3, 1), gap="medium")

with col2:
    st.title("KENO Lottery Number Analysis")

with st.sidebar:
    st.image('images/ca-keno-2x-png.png', width=150)
    col4, col5, col6 = st.columns((.5, 3, .5), gap='small')
    col4 = st.write(" ")
    col5 = st.write("NEXT DRAW")
    next_draw_date_1, count_down_1, last_draw_date_1 = time_until_next_draw(df)
    st.write(next_draw_date_1, unsafe_allow_html=True)
    st.write(count_down_1, unsafe_allow_html=True)
    st.write("<hr>", unsafe_allow_html=True)
    st.write("LAST DRAW", unsafe_allow_html=True)
    st.write(last_draw_date_1)
    last_numbers = last_drawn_numbers(df=df, col_name="Numbers_2")
    st.write(last_numbers)

st.dataframe(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Program Running')





