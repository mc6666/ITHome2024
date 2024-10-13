import pandas as pd
from sqlalchemy import create_engine, inspect
import streamlit as st

@st.cache_data
def get_data(SQL):
    engine = create_engine('sqlite:///./northwind_ORM.db', echo=False)
    df=pd.read_sql(SQL, engine)
    return df
