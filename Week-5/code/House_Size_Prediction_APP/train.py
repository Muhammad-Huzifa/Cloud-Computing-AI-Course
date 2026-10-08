import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from  sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score


dataset = pd.read_csv(r'house_price_dataset.csv')
print(len(dataset))
dataset.head()
dataset.tail()
# print(dataset["Size"])

X = dataset[["Size"]].to_numpy()
print(X.shape)
y = dataset["Price"].to_numpy()
print(X[:5] , y[:5])


X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2 , random_state = 42)

print(X_train.shape)
model = LinearRegression()
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

training = model.fit(X_train_scale , y_train)

prediction = model.predict(X_test_scale)
print(f"Actual_Values: {y_test[:5]}" )
print(f"Predicted_Values: {prediction[:5]}")

Accuracy = r2_score(y_test , prediction)
print(np.round(Accuracy,2))

import joblib
joblib.dump(
model , 
"house_price_model.pkl"
)
joblib.dump(
    scaler , 
    "house_price_scaler.pkl"
)
print("Model and Scaler are Saved")