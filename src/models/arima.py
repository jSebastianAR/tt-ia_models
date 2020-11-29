from shared import csv_utils

def model(path):
    data = csv_utils.get_csv_data(path)
    return data