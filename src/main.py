import os
from models.arima import model as arima_model

cwd = os.getcwd()
data = arima_model(f"{cwd}/datasets/wheather-dataset/14002-ACATLAN DE JUAREZ.csv")

print(data)
