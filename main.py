


## Import the libraries
from variables import data_url, numbers_url
from next_draw_functions import time_until_next_draw, last_drawn_numbers, odds_and_evens, over_under_35, last_three_draws
from tens_csv import tens_csv
from tens_chart_matplot import tens_charts
from number_occurrence_chart import keno_number_count
from number_tracking import number_tracker
from number_tracker_table import number_track_table

import pandas as pd
import streamlit as st

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
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


    title = f"<h4 style = 'font-size:45px; color:#02A161; FONT-FAMILY: Yardmaster Becker liberation serif;'> KENO GAME STATS OVER THE LAST <mark style = 'font-family:liberation serif; font-size:41px; color:#A17512; background-color:transparent;'>{len(df)}</mark> GAMES</h4>"

    st.markdown(f"{title}", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)



    with st.sidebar:
        st.image('images/ca-keno-2x-png.png', width=150)
        col6, col7, col8 = st.columns((.5, 3, .5), gap='small')
        col6 = st.write(" ")
        col7 = st.markdown(f"<H5 style='color:#02A161; font-size:20px;'>  NEXT DRAW </h3>",
                           unsafe_allow_html=True)


        next_draw_date_1, count_down_1, last_draw_date_1 = time_until_next_draw(df)
        st.write(next_draw_date_1, unsafe_allow_html=True)
        col_a, col_b = st.columns((.5,2))
        with col_a:
            st.image("images/time.png", width=30)
        with col_b:
            st.write(f'{count_down_1}' , unsafe_allow_html=True)
        st.write("<hr>", unsafe_allow_html=True)
        st.markdown(f"<H5 style='color:#02A161; font-size:20px;'>  LAST DRAW </h5>",
                           unsafe_allow_html=True)
        st.write(last_draw_date_1)
        last_numbers = last_drawn_numbers(df=df, col_name="Numbers_2")
        st.markdown("<H4 style='color:#A17512 ; font-size: 16px;'> NUMBERS DRAWN (1-70) </h4",
                    unsafe_allow_html=True)
        st.write(last_numbers)

        st.markdown("<H4 style='color:#A17512 ; font-size: 16px;'> OTHER GAME STATS </h4",
                    unsafe_allow_html=True)

        col1, col2, col3 = st.columns((2, 1, 2), gap="medium")
        with col1:
            o_e = odds_and_evens(df, "Odds_vs_Evens")

            st.metric(label="ODD #'s",
                      value=f'{o_e[0]}')
            st.metric(label="EVEN #'s",
                      value=f'{o_e[1]}')

        with col2:
            st.markdown("<p style='border-left:3px solid #02A161; height:130px; marginTop:10px;'> </p>",
                        unsafe_allow_html=True)

        with col3:
            over_under = over_under_35(df=df, col_name="Over_Under_35")
            st.metric(label="1-34",
                      value=f"{over_under[1]}"
                      )
            st.metric(label="35-70",
                      value=f"{over_under[0]}"
                      )

        repeated_numbers = last_drawn_numbers(df=df, col_name="Repeated Numbers")
        three_x = last_three_draws(df=df, col_name="Numbers_2")

        col_d, col_e, col_f = st.columns((2,1,2))
        with col_d:
            st.markdown("REPEATED (2x)")
            st.write(repeated_numbers)

        with col_e:
            st.markdown("<p style='border-left:3px solid #02A161; height:60px; marginTop:5px;'> </p>",
                        unsafe_allow_html=True)

        with col_f:
            st.markdown("REPEATED (3x)")
            st.write(f"{list(three_x)}")


    col9, col10 = st.columns((1,3), gap="medium")
    with col9:
        colnames = ['KENO NUMBERS', 'SELECTED TOTAL']
        df5 = pd.read_csv(numbers_url,
                          header=None,
                          names=colnames
                          )
        fig2 = keno_number_count(df=df5)
        st.pyplot(fig2)

    with col10:
        df_tens = pd.read_csv(
            "data/tens_breakdown.csv",
            parse_dates=True,
            index_col=0)
        fig = tens_charts(df=df_tens)
        st.pyplot(fig=fig)

        st.write(f"Dataframe Documenting KENO GAME STATS Over The Last {len(df)} DRAWS")
        with st.expander(label="🖱️ CLICK TO VIEW TABLE "):
            st.dataframe(df2)

    with st.expander(label="🖱️ CLICK TO VIEW A TABLE TRACKING WHEN NUMBERS WERE DRAWN"):
        number_tracker(df=df, col1="Draw Date", col2="Numbers_2", col3="Time of day")
        fig3 = number_track_table(df='data/keno_numbers_draw_dates.csv')
        st.plotly_chart(fig3)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Program Running')






