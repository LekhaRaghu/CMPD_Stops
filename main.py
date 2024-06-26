import streamlit as st
import pandas as pd

st.write('CMPD Traffic Stops')
st.write('Yaxin Zhao was here!')
@st.cache_data
def load_data(csv):
    df=pd.read_csv(csv)
    return df

stops = pd.read_csv("data/Officer_Traffic_Stops.csv")

st.dataframe(stops)

## Box plot
import altair as alt
alt.Chart(stops).mark_boxplot().encode(
    x = alt.X('Was_a_Search_Conducted'),
    y = alt.Y('Driver_Age')
).properties(
    width = 500,
    title = 'Boxplot between Search Conducted vs Driver Age')