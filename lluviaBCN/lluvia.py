import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import time
from datetime import datetime, timedelta, date, time
import matplotlib.pyplot as plt

infile='download.csv'
pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)

#print(data.describe())
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
anios=data['Any']
enero=data['Precip_Acum_Gener']
febrero=data['Precip_Acum_Febrer']
marzo=data['Precip_Acum_Marc']
abril=data['Precip_Acum_Abril']
mayo=data['Precip_Acum_Maig']
junio=data['Precip_Acum_Juny']
julio=data['Precip_Acum_Juliol']
agosto=data['Precip_Acum_Agost']
septiembre=data['Precip_Acum_Setembre']
octubre=data['Precip_Acum_Octubre']
noviembre=data['Precip_Acum_Novembre']
diciembre=data['Precip_Acum_Desembre']


data['total']=data[['Precip_Acum_Gener','Precip_Acum_Febrer','Precip_Acum_Marc','Precip_Acum_Abril','Precip_Acum_Maig','Precip_Acum_Juny','Precip_Acum_Juliol','Precip_Acum_Agost','Precip_Acum_Setembre','Precip_Acum_Octubre','Precip_Acum_Novembre','Precip_Acum_Desembre']].sum(axis=1)
data['Avg']=data[['Precip_Acum_Gener','Precip_Acum_Febrer','Precip_Acum_Marc','Precip_Acum_Abril','Precip_Acum_Maig','Precip_Acum_Juny','Precip_Acum_Juliol','Precip_Acum_Agost','Precip_Acum_Setembre','Precip_Acum_Octubre','Precip_Acum_Novembre','Precip_Acum_Desembre']].mean(axis=1)
tol=data['total']
avg=data['Avg']
print(data[['Any','total']])

#print(data.groupby('Any').sum())
#lluvias={'Año':anios,'Enero':enero,'Febrero':febrero,'Marzo':marzo,'Abril':abril,'Mayo':mayo,'Junio':junio,'Julio':julio,'Agosto':agosto,'Septiembre':septiembre,'Octubre':octubre,'Noviembre':noviembre,'Diciembre':diciembre}
#Eneros={'Año':anios,'Enero':enero}
Total={'Año':anios,'total':tol}
#df=DataFrame(lluvias,columns=['Año','Enero','Febrero','Marzo','Abril','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])
df=DataFrame(Total,columns=['Año','total'])

df.plot(x='Año',y='total',kind='bar')
plt.show()
#print(anios)

Sep={'Año':anios,'Septiembre':septiembre}
dg=DataFrame(Sep,columns=['Año','Septiembre'])
dg.plot(x='Año',y='Septiembre',ls=':')
plt.title('lluvia Septiembre BCN')
plt.show()