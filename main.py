
from variables import data_url

## import libraries
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
    st.image('images/daily-keno.png', width=150)


st.dataframe(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Program Running')
    print(data_url)




