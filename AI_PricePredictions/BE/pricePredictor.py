import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from pydantic import BaseModel

class PricePredictRequestDTO(BaseModel):
    INT_SQFT: int
    N_BEDROOM: int
    N_BATHROOM: int
    N_ROOM: int
    QS_ROOMS: float
    QS_BATHROOM: float
    QS_BEDROOM: float
    QS_OVERALL: float
    COMMIS: int
    DIST_MAINROAD: int
    PARK_FACIL: int
    AREA: int
    BUILDTYPE: int
    STREET: int

def preprocess_data(df):
    replace_dict = {
        'Ana Nagar': 'Anna Nagar',
        'Ann Nagar': 'Anna Nagar',
        'Karapakkam': 'Karapakam',
        'Chrompt': 'Chrompet',
        'Chrmpet': 'Chrompet',
        'Chormpet': 'Chrompet',
        'KKNagar': 'KK Nagar',
        'TNagar': 'T Nagar',
        'Adyr': 'Adyar',
        'Velchery': 'Velachery',
        'Comercial': 'Commercial',
        'Other': 'Others',
        'AllPub': 'All Pub',
        'NoSewr': 'NoSeWa',
        'NoSewr ': 'NoSeWa',
        'Ab Normal': 'AbNormal',
        'PartiaLl': 'Partial',
        'Partiall': 'Partial',
        'Adj Land': 'AdjLand',
        'Noo': 'No',
        'Pavd': 'Paved',
        'NoAccess': 'No Access'
    }

    df.replace(replace_dict, inplace=True)
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = le.fit_transform(df[col])

    return df

def train_model(df):
    x = df.drop(['SALES_PRICE', 'DATE_SALE', 'DATE_BUILD', 'SALE_COND'], axis=1)
    y = df['SALES_PRICE']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    scaler = MinMaxScaler(feature_range=(0, 5))
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    model = RandomForestRegressor(n_estimators=25)
    model.fit(x_train, y_train)

    return model, scaler




def predict_price(price_predict_request_dto: PricePredictRequestDTO, model, scaler):
    features = np.array([
        price_predict_request_dto.INT_SQFT,
        price_predict_request_dto.N_BEDROOM,
        price_predict_request_dto.N_BATHROOM,
        price_predict_request_dto.N_ROOM,
        price_predict_request_dto.QS_ROOMS,
        price_predict_request_dto.QS_BATHROOM,
        price_predict_request_dto.QS_BEDROOM,
        price_predict_request_dto.QS_OVERALL,
        price_predict_request_dto.COMMIS,
        price_predict_request_dto.DIST_MAINROAD,
        price_predict_request_dto.PARK_FACIL,
        price_predict_request_dto.AREA,
        price_predict_request_dto.BUILDTYPE,
        price_predict_request_dto.STREET
    ]).reshape(1, -1)
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)

    return prediction[0]
# 
# # Read and preprocess data
# df = pd.read_csv("./Housing.csv")
# df = df.dropna()
# df.N_BEDROOM = df.N_BEDROOM.astype('int64')
# df.N_BATHROOM = df.N_BATHROOM.astype('int64')
# df = preprocess_data(df)
# 
# # Train model
# model, scaler = train_model(df)
# 
# # Example usage of predict_price function
# input_features = {
#     'INT_SQFT': 1000,
#     'N_BEDROOM': 1,
#     'N_BATHROOM': 1,
#     'N_ROOM': 1,
#     'QS_ROOMS': 1,
#     'QS_BATHROOM': 1,
#     'QS_BEDROOM': 1,
#     'QS_OVERALL': 1,
#     'COMMIS': 100,
#     'DIST_MAINROAD': 10,
#     'PARK_FACIL': 1,
#     'AREA': 1,
#     'BUILDTYPE': 1,
#     'STREET': 1
# }
# price_predict_request_dto = PricePredictRequestDTO(**input_features)
# price_estimate = predict_price(price_predict_request_dto, model, scaler)
# print("Price estimate:", price_estimate)