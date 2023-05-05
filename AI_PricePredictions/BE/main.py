from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pricePredictor import predict_price, PricePredictRequestDTO, preprocess_data, train_model

# Define the PricePredictRequestDTO class and other functions here

app = FastAPI()

origins = [

    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.post("/predict")
async def predictPrice(predictRequest: PricePredictRequestDTO):
    price_estimate = predict_price(predictRequest, model, scaler)
    
    return {"price_estimate": price_estimate}






# Read and preprocess data
df = pd.read_csv("./Housing.csv")
df = df.dropna()
df.N_BEDROOM = df.N_BEDROOM.astype('int64')
df.N_BATHROOM = df.N_BATHROOM.astype('int64')
df = preprocess_data(df)

# Train model
model, scaler = train_model(df)
