import streamlit as st
import pandas as pd
import altair as alt


@st.cache_data
def load_data(csv):
    df=pd.read_csv(csv)
    return df

stops = load_data("data/Officer_Traffic_Stops.csv")


chart = alt.Chart(stops).mark_bar().encode(
    alt.X('Driver_Age:Q', bin=alt.Bin(maxbins=10)),
    y='count()',
)

# Adding labels and title
chart = chart.properties(
    title='Histogram of Driver Age',
    width=400,  # Adjust the width of the chart as needed
    height=300,  # Adjust the height of the chart as needed
)

# Display the chart
chart

