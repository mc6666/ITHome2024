import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, inspect
from util import *


st.subheader("銷售額年度比較 -- 商品")

SQL = 'select CategoryName from categories order by CategoryID'
df_categories = get_data(SQL)
Categories = st.selectbox(
    "商品類別：", df_categories['CategoryName'].values
)

SQL = f"select * from Product_Sales_YOY where CategoryName = '{Categories}'"        
df = get_data(SQL)
Products = st.multiselect(
    "商品：", df['ProductName'].values, df['ProductName'].values
)
if not Products:
    st.error("Please select at least one category.")
else:
    df = df.query('ProductName in @Products')
    df2 = df.pivot(index='Year', columns='ProductName', values='ProductSales')
    df2
    data = df.pivot(index='ProductName', columns='Year', values='ProductSales')
    st.bar_chart(data=data, stack=False, y=['2017','2018'])
