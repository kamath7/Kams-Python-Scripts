import pandas as pd 

import plotly_express as px 
import streamlit as st

st.set_page_config(page_title="Sales View", page_icon=":bar_chart:",layout="wide")

df = pd.read_excel("./SampleData.xlsx","SalesOrders")
st.dataframe(df)