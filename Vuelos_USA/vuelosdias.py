import pandas as pd
from pandas import DataFrame
import sys
import os
import datetime
#from datetime import date,datetime 

infile = 'flights.csv'
pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)
dia=data['DAY']
mes=data['MONTH']
ano=data['YEAR']
fecha=[]
dias=[]

for i in range(len(dia)):
    fecha.append(datetime.date(ano[i],mes[i],dia[i]))

#print(fecha)
#for i in range(1,366):
#    dias.append(i)
#print(dias)

Datas={'Fecha':fecha}
df=DataFrame(Datas,columns=['Fecha'])

#print(df)
#print()
print(df.groupby('Fecha').size())