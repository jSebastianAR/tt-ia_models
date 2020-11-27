import pandas as pd
import re
import subprocess
import time

def to_csv(list_content,filename,columns):
    COLUMNAS = columns
    town_df = pd.DataFrame(list_content,columns=COLUMNAS)
    town_df.to_csv('csv_dataset/' + filename + '.csv')

def get_csv_data(filename):
    #Lee el .csv
    data = pd.read_csv(filename)
    return data

def main():
    get_csv_data('')
    

if __name__ == '__main__':
    main()