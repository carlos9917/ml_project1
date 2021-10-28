import streamlit as st
import pandas as pd
import base64
#import matplotlib.pyplot as plt
#import matplotlib.dates as md
#from matplotlib.ticker import MaxNLocator
#import seaborn as sns
import numpy as np
#import yfinance as yf
#import sqlite3
from datetime import datetime
from datetime import timedelta
from collections import OrderedDict

st.title('Appliances prediction')

st.markdown("""
This app calculates an appliance consumption
based on the user input. \n
It can be several of the following features:
Humidity (%), Temperature (Celsius), Light (Watts)
""")

# Read the sqlite file
def load_model(model_file="random_forest.bin"):
    import pickle
    with open(model_file, 'rb') as f_in:
         model = pickle.load(f_in)
    return model

st.sidebar.header('User Input Parameters')

def user_input_features():
    humidity = st.sidebar.slider('Humidity inside', 10, 100, 10)
    temperature={}
    temperature["T1"] = st.sidebar.slider('Temperature sensor 1', 5, 30, 1)
    temperature["T2"] = st.sidebar.slider('Temperature sensor 2', 5, 30, 1)
    temperature["T3"] = st.sidebar.slider('Temperature sensor 3', 5, 30, 1)
    temperature["T4"] = st.sidebar.slider('Temperature sensor 4', 5, 30, 1)
    temperature["T5"] = st.sidebar.slider('Temperature sensor 5', 5, 30, 1)
    temperature["T6"] = st.sidebar.slider('Temperature sensor 6', 5, 30, 1)
    temperature["T7"] = st.sidebar.slider('Temperature sensor 7', 5, 30, 1)
    temperature["T8"] = st.sidebar.slider('Temperature sensor 8', 5, 30, 1)
    temperature["T9"] = st.sidebar.slider('Temperature sensor 9', 5, 30, 1)
    temp_out = 20 #st.sidebar.slider("Temperature outside",1,30,1)
    hum_out = 60 #st.sidebar.slider("Humidity outside",10,100,10)
    light = st.sidebar.slider('Light intensity (Watts)', 0, 70, 10)
    data={} 
    
    for col in ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9']:
        data[col] = temperature[col]

    for col in ['RH_1', 'RH_2', 'RH_3', 'RH_4', 'RH_5', 'RH_6', 'RH_7', 'RH_8', 'RH_9']:
        data[col] = humidity

    data["lights"] = light
    data["T_out"] = temp_out
    data["RH_out"] = hum_out
    for col in ['Press_mm_hg', 'Windspeed', 'Visibility', 'lights','Tdewpoint']:
        data[col] = 0.0
    features = pd.DataFrame(data, index=[0])


    return features
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)
rf = load_model()
prediction = rf.predict(df)
st.subheader('Prediction (Watts)')
print(np.exp(prediction))
st.write(np.exp(prediction))
#st.write(prediction)


def calculate_prediction(data):
    '''
    Count days present for all days,
    starting at the beginning of each year
    Return a data frame with dates and number of days produced on each day
    '''
    return data_count
