from shared import csv_utils
from shared import plot_data
import numpy as np
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
from statsmodels.tsa.arima_model import ARIMA

#['FECHA','PRECIP(mm)','EVAP(mm)','TMAX(°C)','TMIN(°C)']

class Arima():
    def __init__(self, data_path):
        self.dataFrame = csv_utils.get_csv_data(data_path,'TMAX(°C)')
        #Grafica los datos
        plot_data.graph_data(self.dataFrame,'TMAX(°C)')
        #Evalua si los datos son estacionarios
        self.ad_test(self.dataFrame['TMAX(°C)'])
        #Encuentra el orden adecuado del modelo arima para los datos
        self.getModelOrder(self.dataFrame['TMAX(°C)'])
        #Resultado: ARIMA(2,1,3)(0,0,0)[0]             : AIC=16098.607, Time=1.19 sec
        #Obtiene el conjunto de entrenamiento y testing
        self.getTrainAndTest(self.dataFrame['TMAX(°C)'])


    def ad_test(self,dataset):
        """
        Test para probar que los datos sean estacionarios
        
        Si p <0,05; Los datos son estacionarios

        si p> 0,05; Los datos no son estacionarios"""

        dftest = adfuller(dataset, autolag = 'AIC')
        print("1. ADF : ",dftest[0])
        print("2. P-Value : ", dftest[1])
        print("3. Num Of Lags : ", dftest[2])
        print("4. Num Of Observations Used For ADF Regression:",      dftest[3])
        print("5. Critical Values :")
        for key, val in dftest[4].items():
            print("\t",key, ": ", val)

        if dftest[1] < 0.05:
            print('Es estacionaria')
        else:
            print('No es estacionaria')

    def getModelOrder(self,data):
        stepwise_fit = auto_arima(data, trace=True,
        suppress_warnings=True)

    def getTrainAndTest(self,df):
        print(df.shape)
        train=df.iloc[:-365] #Toma los primeros, exceptuando los días del año 2018
        test=df.iloc[-365:] #Toma los días del año 2018
        print(train.shape, test.shape)
        return train, test
