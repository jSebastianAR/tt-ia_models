import pandas as pd
import re
import subprocess
import time

def to_csv(list_content,filename,columns):
    COLUMNAS = columns
    town_df = pd.DataFrame(list_content,columns=COLUMNAS)
    town_df.to_csv('csv_dataset/' + filename + '.csv')

def get_csv_data(filename,param):
    #Lee el .csv
    df = pd.read_csv(filename)
    return df

def main():
    #get_csv_data('')
    pass
    

if __name__ == '__main__':
    main()