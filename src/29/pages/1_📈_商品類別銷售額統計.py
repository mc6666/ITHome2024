import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, inspect
from util import *

st.subheader("銷售額統計 -- 商品類別")

SQL = 'select * from Category_Sales'
df = get_data(SQL)
# print('*** Category:', df['CategoryName'].values)
Categories = st.multiselect(
    "商品類別：", df['CategoryName'].values, df['CategoryName'].values
)
if not Categories:
    st.error("Please select at least one category.")
else:
    df = df.query('CategoryName in @Categories')
    st.bar_chart(data=df, x='CategoryName', y='CategorySales')
