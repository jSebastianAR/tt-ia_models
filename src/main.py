import os
from models.arima import Arima
from shared import csv_utils

cwd = os.getcwd()

arima_model = Arima(f"{cwd}/datasets/wheather-dataset/14002-ACATLAN DE JUAREZ.csv")

#print(arima_model.data)
