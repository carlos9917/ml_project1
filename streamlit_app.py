import streamlit as st
import pandas as pd
import base64
#import matplotlib.pyplot as plt
#import matplotlib.dates as md
#from matplotlib.ticker import MaxNLocator
#import seaborn as sns
import numpy as np
import os
#import yfinance as yf
#import sqlite3
from datetime import datetime
from datetime import timedelta
from collections import OrderedDict

st.title('Appliances prediction')

st.markdown("""
This app calculates an appliance consumption
based on the user input. \n
Currently the user can vary only the 9 temperature sensors
inside the room, as well as the light intensity. \n
Setting the humidity inside (%) will set all sensors to the same value.
Temperature (Celsius)
""")

# Read the sqlite file
def load_model(model_file="random_forest.bin"):
    import pickle
    with open(model_file, 'rb') as f_in:
         model = pickle.load(f_in)
    return model

st.sidebar.header('User Input Parameters')

def user_input_features():
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
    humidity={}
    
    humidity["RH_1"] = st.sidebar.slider('Relative Humidity sensor 1', 30, 100, 10)
    humidity["RH_2"] = st.sidebar.slider('Relative Humidity sensor 2', 30, 100, 10)
    humidity["RH_3"] = st.sidebar.slider('Relative Humidity sensor 3', 30, 100, 10)
    humidity["RH_4"] = st.sidebar.slider('Relative Humidity sensor 4', 30, 100, 10)
    humidity["RH_5"] = st.sidebar.slider('Relative Humidity sensor 5', 30, 100, 10)
    humidity["RH_6"] = st.sidebar.slider('Relative Humidity sensor 6', 30, 100, 10)
    humidity["RH_7"] = st.sidebar.slider('Relative Humidity sensor 7', 30, 100, 10)
    humidity["RH_8"] = st.sidebar.slider('Relative Humidity sensor 8', 30, 100, 10)
    humidity["RH_9"] = st.sidebar.slider('Relative Humidity sensor 9', 30, 100, 10)

    light = st.sidebar.slider('Lights use (Wh)', 0, 70, 10)

    #set the data:
    data={} 
    for col in ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9']:
        data[col] = temperature[col]
    for col in ['RH_1', 'RH_2', 'RH_3', 'RH_4', 'RH_5', 'RH_6', 'RH_7', 'RH_8', 'RH_9']:
        data[col] = 80 #humidity[col]

    data["lights"] = light

    #These values are updated from the last weather data that
    #it was available at the moment of deployment
    if os.path.isfile("./scrap_weather_data/weather_data.csv"):
        weather_data = pd.read_csv("./scrap_weather_data/weather_data.csv")
    data["Visibility"] = 0 #not found in weather data, setting to fixed value
    temp_out = 20
    hum_out = 60
    data["T_out"] = temp_out
    data["RH_out"] = hum_out
    for col in ["T_out","RH_out",'Press_mm_hg', 'Windspeed', 'Tdewpoint']:
        #data[col] = 0.0
        data[col]=weather_data[col].values[0]
    print("Using weather data")
    print(data)
    features = pd.DataFrame(data, index=[0])


    return features
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)
rf = load_model()
prediction = rf.predict(df)
st.subheader('Consumption prediction (Wh)')
print(np.exp(prediction))
st.write(np.exp(prediction[0]))
#st.write(prediction)


def calculate_prediction(data):
    '''
    Count days present for all days,
    starting at the beginning of each year
    Return a data frame with dates and number of days produced on each day
    '''
    return data_count
