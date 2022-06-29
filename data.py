import numpy as np  
import pandas as pd
import streamlit as st
# S6.3: Divide the web page into three columns to add more widgets.
def app(car_df):
  st.header('View Data')
  with st.beta_expander('View dataset'):
    st.write(car_df)

  st.subheader('Column Description:')
  if st.checkbox('Show Summary:'):
    st.table(car_df.describe())

  beta_col1, beta_col2, beta_col3=st.beta_columns(3)
  with beta_col1:
    if st.checkbox('Show all Column Names'):
      st.table(list(car_df.columns))
  with beta_col2:
    if st.checkbox('View Column DataType'):
      st.table(car_df.dtypes)# likewise for series we use dtype
  with beta_col3:
    if st.checkbox('View Column Data'):
      cols=st.selectbox('Select Column', tuple(car_df.columns))
      st.write(car_df[cols])