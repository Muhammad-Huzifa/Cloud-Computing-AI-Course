from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import joblib

df = pd.read_csv('Housing.csv')

# print(df.head())
features = [
    "area",
    "bedrooms",
    "bathrooms",
    "stories",
    "parking"
]

X = df[features].to_numpy()
y = df["price"].to_numpy()

print(len(X)) , print( len(y))

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2 , random_state= 42 )

print(X_train.shape)

scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scale , y_train)

y_pred = model.predict(X_test_scale)
print(f"Actual_Value: {y_test[:4]} , Prediction: {y_pred[:4]}")

r2 = r2_score(y_test , y_pred)
print(r2)

joblib.dump(
    model , "ml-regression-model.pkl"
)
joblib.dump(
    scaler , "ml-regression-scaler.pkl"
)
