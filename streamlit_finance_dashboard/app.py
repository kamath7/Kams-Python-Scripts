import pandas as pd

import plotly_express as px
import streamlit as st

st.set_page_config(page_title="Sales View",
                   page_icon=":bar_chart:", layout="wide")
@st.cache
def get_data():
    df = pd.read_excel("./SampleData.xlsx", "SalesOrders")
    return df

df = get_data()
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

df_selection = df.query("Region == @region & Item == @item")


st.dataframe(df_selection)

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

total_units_sold = int(df_selection["Units"].sum())
total_units_cost = int(df_selection["Unit Cost"].sum())
total_sale = int(df_selection["Total"].sum())

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Units sold")
    st.subheader(f"{total_units_sold}")

with middle_column:
    st.subheader("Total Units sold Cost")
    st.subheader(f"{total_units_cost}")
with left_column:
    st.subheader("Total Sale")
    st.subheader(f"{total_sale}")

st.markdown("---")

sales_by_product = (
    df_selection.groupby(by=["Item"]).sum()[["Total"]].sort_values(by="Total")
)
product_sales_graph = px.bar(sales_by_product, x="Total", y = sales_by_product.index, orientation="h", title ="<b>Sales by Product</b>", color_discrete_sequence=["#008388"] * len (sales_by_product), template="plotly_white")
# product_sales_graph = px.bar(sales_by_product, x="Total", y=sales_by_product, orientation="h", title="<b>Sales by Product</b>")
st.plotly_chart(product_sales_graph)

#next to-do - figure out on how flask can serve this