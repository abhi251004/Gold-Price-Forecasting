#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing the required libaries
import numpy as np
import pandas as pd
from pandas.tseries.offsets import DateOffset
import streamlit as st 
import scipy.stats as stats
#Data Driven Methods
import statsmodels
from statsmodels.tsa.api import ExponentialSmoothing
from statsmodels.base.model import Results
from statsmodels.base.wrapper import ResultsWrapper
import pickle
from pickle import dump
from pickle import load


#Title of the Site
st.title('Forecasting of Gold Price')

ori = pd.read_pickle("GoldPriceforecast.pickle")

future_dates = [ori.index[-1] + DateOffset(years=x)for x in range(0,52)]
future_df = pd.DataFrame(index=future_dates[1:],columns=ori.columns)
future_df.index.name = "Gold Price"

st.header('Select the Year')
user_input = st.slider('Year Slider', , 2065)
year = user_input - 2014
loc = year - 1

# load the model from disk
#loaded_model = load(open('air_quality_forecast.sav', 'rb'))
loaded_model = load(open('air_quality_forecasts.pickle', 'rb'))

#Prediction
predict = loaded_model.predict(start=future_df.index[0],end=future_df.index[-1])
future_df['CO2']= np.exp(predict)

#Creating a Dictionary for DataFrame
result = {
    "Year":user_input,
    "Forecast":future_df['CO2'].iloc[loc]
}

#Creating a DataFrame
final_result = pd.DataFrame(result, index = [0])

st.subheader('Forecasted Result')
st.write(final_result)

