import streamlit as st
import pandas as pd

# 測試資料
df = pd.read_csv("https://streamlit-demo-data.s3-us-west-2.amazonaws.com/agri.csv.gz")

# 顯示 DataFrame
df