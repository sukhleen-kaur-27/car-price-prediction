# S2.1: Import the necessary Python modules and create the 'prediction()' function as directed above.
# Importing the necessary Python modules.
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_squared_log_error

# Define the 'prediction()' function.
@st.cache()
def prediction(car_df, carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick):
  X=car_df.iloc[:,:-1]
  y=car_df['price']
  X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=42)
  
  lr=LinearRegression(n_jobs=-1)
  lr.fit(X_train, y_train)
  lr_score=lr.score(X_train, y_train)
  pred=lr.predict([[carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick]])
  pred=pred[0]

  y_test_pred=lr.predict(X_test)
  r2_test_score=r2_score(y_test, y_test_pred)
  mae_test=mean_absolute_error(y_test, y_test_pred)
  mean_squared_test_error=mean_squared_error(y_test, y_test_pred)
  rmse_test=np.sqrt(mean_squared_test_error)
  msle_test=mean_squared_log_error(y_test, y_test_pred)

  return pred, lr_score, r2_test_score, mae_test, rmse_test, msle_test

# S2.2: Define the 'app()' function as directed above.
def app(car_df):
  st.markdown("<p style='color:blue;font-size:25px'> This app uses <b>Linear Regression</b> to predict the price of a car based on your inputs. </p>", unsafe_allow_html=True)
  st.subheader('Select Value')
  carwidth=st.slider('Select carwidth', float(car_df['carwidth'].min()), float(car_df['carwidth'].max()))
  enginesize=st.slider('Select enginesize', int(car_df['enginesize'].min()), int(car_df['enginesize'].max()))
  horsepower=st.slider('Select horsepower', int(car_df['horsepower'].min()), int(car_df['horsepower'].max()))
  drivewheel_fwd=st.radio('Is it forward drive wheelcar?', ('Yes', 'No'))
  car_company_buick=st.radio('Is the car manufactured by buick?', ('Yes', 'No'))
  if car_company_buick=='Yes':
    car_company_buick=1
  else:
    car_company_buick=0
  if drivewheel_fwd=='Yes':
    drivewheel_fwd=1
  else:
    drivewheel_fwd=0
  if st.button('Predict'):
    st.subheader('Prediction Results')
    price, score, r2_test_score, mae_test, rmse_test, msle_test=prediction(car_df, carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick)
    st.success(f'The predicted price of the car is {round(price,2)}')
    st.info(f'Accuracy score of the linear regression model is {round(score,2)}')
    st.info(f'R2 score of the linear regression model is {round(r2_test_score,2)}')
    st.info(f'Mean Absolute Error for testing dataset {round(mae_test,2)}')
    st.info(f'Root Mean Squared Error for testing dataset {round(rmse_test,2)}')
    st.info(f'Mean Squared Log Error for testing dataset {round(msle_test,2)}')
