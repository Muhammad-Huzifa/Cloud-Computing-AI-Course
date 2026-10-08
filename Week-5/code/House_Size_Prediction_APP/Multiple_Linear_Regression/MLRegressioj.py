from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import joblib

df = pd.read_csv(r"C:\Users\Muhammad Huzifa\Desktop\Huawei_HCCDA_AI\Cloud-Computing-AI-Course\Cloud-Computing-AI-Course\Week-5\code\House_Size_Prediction_APP\Multiple_Linear_Regression\Housing.csv")
df.shape