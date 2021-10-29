# Importing the FastApi class
from fastapi import FastAPI
import pandas as pd

# Creating an app object
app = FastAPI()

# Post -- > Create new prediction
@app.put("/measurements", tags=["MEASUREMENTS"])
async def add_features(body: dict) -> dict:
    for key in body.keys():
        user_input[key] = body[key]
    #customer["contract"] = body["contract"]
    #customer["tenure"] = body["tenure"]
    #customer["monthlycharges"] = body["monthlycharges"]
    return body

@app.post("/predict", tags=['PREDICT APPLIANCE CONSUMPTION'])
async def predict() -> dict:
    return {"Model output": prediction}

def get_model():
    import pickle
    model_file = 'random_forest.bin'
    with open(model_file, 'rb') as f_in:
         model = pickle.load(f_in)
    return model



#Filling up this with some default values

user_input = {
"lights": 30,
"T1":  19.89,
"RH_1" : 47.5967,
"T2":   19.2,
"T3":     19.79,
"T4":        19,
"T5":   17.1667,
"T6":   7.02667,
"T7":      17.2,
"T8":      18.2,
"T9":   17.0333,
"RH_2":  44.79,
"RH_3":  44.73,
"RH_4":45.5667,
"RH_5":   55.2,
"RH_6":84.25672,
"RH_7":41.6267,
"RH_8":  48.9,
"RH_9":  45.53,
"T_out":  6.6,
"Press_mm_hg": 733.5,
"RH_out":        92,
"Windspeed":      7,
"Visibility":    63,
"Tdewpoint":    5.3,
"T_out": 7.0, 
    }
features = pd.DataFrame(user_input, index=[0])

model = get_model()
y_pred = model.predict(features)

prediction = [ {
         "features": user_input,
         "Appliances": float(y_pred) }
]


