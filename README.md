# midterm project for Alex Grigoriev ML Zoomcamp

## Project

Appliances energy prediction

[Data set](https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction)
Predict appliance consumption from 10 min measurements over 4.5 months
inside a house, where temperature and humidity conditions were monitored with a ZigBee wireless sensor network. 
The energy data was logged every 10 minutes with m-bus energy meters. 

Weather data is included, taken from the nearest airport weather station (Chievres Airport, Belgium).
I doubt such data will have much effect on the prediction, since it is measured outside
of the room and the number of sensors inside (9 each for temp and humidity) is far greater.

Two random variables were also included in the data set for testing the regression models and to filter out non predictive attributes (parameters). Not sure what the hell this means, haven't read the paper!


## EDA and model development

Included in jupyter notebook. 
Final model is trained there and saved in a pickle file.

## Deployment

There are two options for deployment.
### Fast api
One is local, using the provided Dockerfile
and a fast-api webapp.
To run the app locally use the main.py file
python main.py
and open the localhost indicated in link
Then open:
http://127.0.0.1:8000/docs

Not very pretty, but it works.
The second option is more visually appealing

### streamlit
The second app is deployed with streamlit. The app has been
uploaded here:
https://share.streamlit.io/carlos9917/ml_project1
Simply follow instructions in webapp to test.
All the source code is included in this repo.
