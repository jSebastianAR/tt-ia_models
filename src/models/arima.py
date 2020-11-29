from shared import csv_utils

class Arima():
    def __init__(self, data_path):
        self.data = csv_utils.get_csv_data(data_path)