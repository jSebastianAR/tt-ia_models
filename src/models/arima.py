from shared import csv_utils
from shared import plot_data
import numpy as np
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
#from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

#['FECHA','PRECIP(mm)','EVAP(mm)','TMAX(°C)','TMIN(°C)']

class Arima():

    def __init__(self, data_path):
        self.name = self.get_name(data_path)
        print(self.name)
        self.param = 'TMAX(°C)'
        self.dataFrame = csv_utils.get_csv_data(data_path,self.param)
        #Grafica los datos
        plot_data.graph_data(self.dataFrame,self.param)
        #Evalua si los datos son estacionarios
        self.ad_test(self.dataFrame[self.param])
        #Encuentra el orden adecuado del modelo arima para los datos
        self.getModelOrder(self.dataFrame[self.param])
        #Resultado: ARIMA(2,1,3)(0,0,0)[0]             : AIC=16098.607, Time=1.19 sec
        #Obtiene el conjunto de entrenamiento y testing
        train, test = self.getTrainAndTest(self.dataFrame)
        #Entrena el modelo
        model = self.fit_model(train[self.param],self.name)
        #Testea el modelo
        self.test_model(model,train[self.param],test[self.param])



    def ad_test(self,dataset):
        """
        Test para probar que los datos sean estacionarios
        
        Si p <0,05; Los datos son estacionarios

        si p> 0,05; Los datos no son estacionarios"""

        #dftest = adfuller(dataset, autolag = 'AIC')
        dftest = adfuller(dataset)
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

        stepwise_fit.summary()

    def getTrainAndTest(self,df):
        print(df.shape)
        train=df.iloc[:-365] #Toma los primeros, exceptuando los días del año 2018
        test=df.iloc[-365:] #Toma los días del año 2018
        print(train.shape, test.shape)
        return train, test

    def fit_model(self,train_data,namefile):
        model=ARIMA(train_data,order=(2,1,3),enforce_stationarity=True)
        model=model.fit()
        model.summary()
        model.save(namefile + '.pickle')
        return model


    def test_model(self,model,train_data,test_data):
        start=len(train_data)
        end=len(train_data)+len(test_data)-1
        pred=model.predict(start=start,end=end,typ='levels').rename('ARIMA Predictions')
        pred.plot(legend=True)
        test_data.plot(legend=True)
        plt.show()

    def get_name(self,data_path):

        parts = data_path.split('/')
        txt = parts[len(parts)-1]
        name_file = txt.split('.csv')
        return name_file[0]
