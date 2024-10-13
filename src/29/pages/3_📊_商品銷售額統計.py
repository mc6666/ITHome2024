import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, inspect
from util import *

st.subheader("銷售額統計 -- 商品")

SQL = 'select CategoryName from categories order by CategoryID'
df_categories = get_data(SQL)
Categories = st.selectbox(
    "商品類別：", df_categories['CategoryName'].values
)

SQL = f"select * from Product_Sales where CategoryName = '{Categories}'"        
# SQL = "select Products.ProductName," \
    # + " Sum(([Order Details].UnitPrice*Quantity*(1-Discount)/100)*100) AS ProductSales" \
    # + " from Categories JOIN Products " \
    # + " On Categories.CategoryID = Products.CategoryID" \
    # + " JOIN  [Order Details] on Products.ProductID = [Order Details].ProductID" \
    # + " JOIN  [Orders] on Orders.OrderID = [Order Details].OrderID" \
    # + f" where CategoryName = '{Categories}'" \
    # + " and Orders.ShippedDate Between DATETIME('2017-01-01') And DATETIME('2017-12-31')" \
    # + " GROUP BY Categories.CategoryName, Products.ProductName"        
df = get_data(SQL)
# print('*** Category:', df['CategoryName'].values)
Products = st.multiselect(
    "商品：", df['ProductName'].values, df['ProductName'].values
)
if not Products:
    st.error("Please select at least one Product.")
else:
    # df = df.set_index('CategoryName')
    df = df.query('ProductName in @Products')
    st.bar_chart(data=df, x='ProductName', y='ProductSales')
