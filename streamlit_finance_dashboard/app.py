import pandas as pd 

import plotly_express as px 
import streamlit as st

st.set_page_config(page_title="Sales View", page_icon=":bar_chart:",layout="wide")

df = pd.read_excel("./SampleData.xlsx","SalesOrders")
st.dataframe(df)

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select the region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)
item = st.sidebar.multiselect(
    "Select the Item",
    options=df["Item"].unique(),
    default=df["Item"].unique()
)

