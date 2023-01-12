import datetime

import pytz

## Import the libraries
from variables import data_url, numbers_url
from next_draw_functions import time_until_next_draw, last_drawn_numbers, odds_and_evens, over_under_35, last_three_draws
from tens_csv import tens_csv
from tens_chart_matplot import tens_charts
from number_occurrence_chart import keno_number_count
from number_tracking import number_tracker
from number_tracker_table import number_track_table
from keno_numbers_table import keno_table
from random_number_generator import quick_picks

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


    df2 = df[['Draw Date', 'Time of day', 'Numbers_2', 'Odds_vs_Evens', 'Over_Under_35', 'Repeated Numbers', \
              'Consecutive_Numbers', 'Tens_Category', 'Sum_of_picks',
              ]]

    col_i, col_j, col_k = st.columns((2,0.5, 1))
    with col_i:
        title = f"<h1 style = 'font-size:50px; color:#02A161;'> KENO GAME STATS OVER <br>THE LAST <mark style = 'font-family:liberation serif; font-size:55px; color:#A17512; background-color:transparent;'>{len(df)}</mark> GAMES</h1>"
        st.markdown(f"{title}", unsafe_allow_html=True)

    with col_j:
        st.markdown("<p style='border-left:3px solid #02A161; height:240px; marginTop:10px;'> </p>",
                    unsafe_allow_html=True)

    with col_k:
        st.markdown(
            "<H4 style='color:#A17512 ; font-size: 27px;'> QUICK PICKS  </h4>",
            unsafe_allow_html=True)
        with st.form(key="quick_pick_selection"):
            #submitted = st.form_submit_button(label="Get Numbers")
            st.markdown("<H4 style='color:lightyellow ; font-size: 18px;'> How many numbers do you want? </h4",
                        unsafe_allow_html=True)
            #st.image(image='images/ball_selection.png', width=40)
            numbers = st.select_slider('', [2,3,5,6,7,8,8,9,10])
            submitted = st.form_submit_button(label="Get Numbers")
            quick_picks = quick_picks(n=numbers)
            #st.write(quick_picks)

            # st.markdown(f"<p style='color:#A17512 ; font-size: 20px;'> {quick_picks[0]} , {quick_picks[1]} </p> ",
            #             unsafe_allow_html=True)
            if submitted:
                st.success(f"Here are your {numbers} Quick Pick numbers")
                st.balloons()
                st.markdown(f"<p style='color:#A17512 ; font-size: 26px; border-style:solid;border-color:#02A161; text-align:center; padding:5px;'> {quick_picks} </p> ", unsafe_allow_html=True)
            else:
                st.markdown(f"<p style='color:lightyellow ; font-size: 14px; border-style:solid;border-color:#02A161; padding:5px;text-align:center;'>---- quick picks ----</p> ", unsafe_allow_html=True)


    st.markdown("---", unsafe_allow_html=True)



    with st.sidebar:
        col_q, col_r = st.columns((1,1))
        with col_q:
            st.image('images/ca-keno-2x-png.png', width=140)
        with col_r:
            st.markdown("<br>", unsafe_allow_html=True)
            st.write(f"<H5 style='color:#02A161; font-size:14px;'> {datetime.datetime.now(tz=pytz.timezone('EST')).strftime('%A %B %#d, %Y %H:%M:%S%p %Z')} </h5>",
                     unsafe_allow_html=True)

        col6, col7, col8 = st.columns((.5, 3, .5), gap='small')
        col6 = st.write(" ")
        col7 = st.markdown(f"<H5 style='color:#02A161; font-size:20px;'>  NEXT DRAW </h3>",
                           unsafe_allow_html=True)


        next_draw_date_1, next_draw_time_1, count_down_1, last_draw_date_1 = time_until_next_draw(df)
        col_o, col_p = st.columns((0.4, 2))
        with col_o:
            st.image("images/calendar.png", width=30)
        with col_p:
            st.write(next_draw_date_1, unsafe_allow_html=True)
        col_a, col_b = st.columns((.4,2))
        with col_a:
            st.image("images/time.png", width=30)
        with col_b:
            st.write(f"<mark style = 'font-family:liberation serif; font-size:17px; color:#A17512; background-color:transparent;'>{count_down_1}</mark>  {next_draw_time_1} " , unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
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
        st.markdown("<H4 style='color:#A17512 ; font-size: 26px;'> RUNNING COUNT OF EACH \n KENO NUMBER DRAWN </h4",
                    unsafe_allow_html=True)
        st.pyplot(fig2)

    with col10:
        df_tens = pd.read_csv(
            "data/tens_breakdown.csv",
            parse_dates=True,
            index_col=0)
        fig = tens_charts(df=df_tens)
        st.markdown("<H4 style='color:#A17512 ; font-size: 26px;'> COUNT OF THE OCCURRENCES<br> OF EACH 10's DIGITS </h4",
                    unsafe_allow_html=True)
        st.pyplot(fig=fig)

        st.markdown(
            f"<H4 style='color:#A17512 ; font-size: 26px;'> Dataframe Documenting KENO GAME STATS Over The Last {len(df)} DRAWS </h4>",
            unsafe_allow_html=True)
        #st.write(f"Dataframe Documenting KENO GAME STATS Over The Last {len(df)} DRAWS")
        with st.expander(label="🖱️ CLICK TO VIEW TABLE "):
            st.dataframe(df2)

    st.markdown(
        f"<H4 style='color:#A17512 ; font-size: 26px;'> A Table Tracking When Each Number Has Been Drawn Over The Past 20 DRAWS </h4>",
        unsafe_allow_html=True)
    with st.expander(label="🖱️ CLICK TO VIEW TABLE"):
        number_tracker(df=df, col1="Draw Date", col2="Numbers_2", col3="Time of day")
        fig3 = number_track_table(df='data/keno_numbers_draw_dates.csv')
        fig4 = keno_table()
        col_z, col_y = st.columns((1, 10))
        with col_z:
            st.plotly_chart(fig4)
        with col_y:
            st.plotly_chart(fig3)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Program Running')






