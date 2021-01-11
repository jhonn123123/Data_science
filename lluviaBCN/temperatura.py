import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import time
from datetime import datetime, timedelta, date, time
import matplotlib.pyplot as plt

infile='download2.csv'
pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)

#print(data.describe())
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
anios=data['Any']
enero=data['Temp_Mitjana_Gener']
febrero=data['Temp_Mitjana_Febrer']
marzo=data['Temp_Mitjana_Marc']
abril=data['Temp_Mitjana_Abril']
mayo=data['Temp_Mitjana_Maig']
junio=data['Temp_Mitjana_Juny']
julio=data['Temp_Mitjana_Juliol']
agosto=data['Temp_Mitjana_Agost']
septiembre=data['Temp_Mitjana_Setembre']
octubre=data['Temp_Mitjana_Octubre']
noviembre=data['Temp_Mitjana_Novembre']
diciembre=data['Temp_Mitjana_Desembre']


data['total']=data[['Temp_Mitjana_Gener','Temp_Mitjana_Febrer','Temp_Mitjana_Marc','Temp_Mitjana_Abril','Temp_Mitjana_Maig','Temp_Mitjana_Juny','Temp_Mitjana_Juliol','Temp_Mitjana_Agost','Temp_Mitjana_Setembre','Temp_Mitjana_Octubre','Temp_Mitjana_Novembre','Temp_Mitjana_Desembre']].sum(axis=1)
data['Avg']=data[['Temp_Mitjana_Gener','Temp_Mitjana_Febrer','Temp_Mitjana_Marc','Temp_Mitjana_Abril','Temp_Mitjana_Maig','Temp_Mitjana_Juny','Temp_Mitjana_Juliol','Temp_Mitjana_Agost','Temp_Mitjana_Setembre','Temp_Mitjana_Octubre','Temp_Mitjana_Novembre','Temp_Mitjana_Desembre']].mean(axis=1)
tol=data['total']
avg=data['Avg']
print(data[['Any','Avg']])

#print(data.groupby('Any').sum())
#lluvias={'Año':anios,'Enero':enero,'Febrero':febrero,'Marzo':marzo,'Abril':abril,'Mayo':mayo,'Junio':junio,'Julio':julio,'Agosto':agosto,'Septiembre':septiembre,'Octubre':octubre,'Noviembre':noviembre,'Diciembre':diciembre}
#Eneros={'Año':anios,'Enero':enero}
Total={'Año':anios,'Avg':avg}
#df=DataFrame(lluvias,columns=['Año','Enero','Febrero','Marzo','Abril','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
df=DataFrame(Total,columns=['Año','Avg'])

df.plot(x='Año',y='Avg',color='m',kind='bar')
plt.title('Promedio de Temperatura por año en BCN')
plt.show()