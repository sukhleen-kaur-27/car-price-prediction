# S1.1: Design the "Visualise Data" page of the multipage app.
# Import necessary modules 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Define a function 'app()' which accepts 'car_df' as an input.

def app(car_df):
  st.header('Visualise Data')
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.subheader('Scatter Plot')
  scatter_cols=st.multiselect('Select x-axis values:', ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for col in scatter_cols:
    st.subheader(f'Scatter Plot between {col} and price')
    plt.figure(figsize=(12,6))
    sns.scatterplot(x=col, y='price', data=car_df)
    st.pyplot()
  
  st.subheader('Visualisation Selector')
  plots=st.multiselect('Select Charts/Plots:', ('Histogram', 'Boxplot', 'Correlation Heatmap'))

  if 'Histogram' in plots:
    st.subheader('Histogram')
    column=st.selectbox('Select the column to create its histogram', ('carwidth', 'enginesize', 'horsepower'))
    plt.figure(figsize=(12,6))
    plt.title(f'Histogram for {column}')
    plt.hist(car_df[column], bins='sturges', edgecolor='black')
    st.pyplot()

  if 'Boxplot' in plots:
    st.subheader('Boxplot')
    column=st.selectbox('Select the column to create its boxplot', ('carwidth', 'enginesize', 'horsepower'))
    plt.figure(figsize=(12,6))
    plt.title(f'Boxplot for {column}')
    sns.boxplot(car_df[column])
    st.pyplot()

  if 'Correlation Heatmap' in plots:
    st.subheader('Correlation Heatmap')
    plt.figure(figsize=(14,14))
    hm=sns.heatmap(car_df.corr(), annot=True, square=True)
    bottom, top=hm.get_ylim()
    hm.set_ylim(bottom+0.5, top-0.5)
    st.pyplot()