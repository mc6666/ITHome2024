import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, inspect
from util import *


st.subheader("銷售額年度比較 -- 商品類別")

SQL = "select * from Category_Sales_YOY"        
df = get_data(SQL)
Categories = st.multiselect(
    "商品類別：", df['CategoryName'].values, df['CategoryName'].values
)
if not Categories:
    st.error("Please select at least one category.")
else:
    # df = df.set_index('CategoryName')
    df = df.query('CategoryName in @Categories')
    df2 = df.pivot(index='Year', columns='CategoryName', values='ProductSales')
    df2
    data = df.pivot(index='CategoryName', columns='Year', values='ProductSales')
    st.bar_chart(data=data, stack=False, y=['2017','2018'])
