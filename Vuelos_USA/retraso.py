import pandas as pd
from pandas import DataFrame
import numpy as np
import sys
import os
import statistics
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats


infile = 'flights.csv'
buscar = 'ARRIVAL_DELAY'

pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)
delay=data['ARRIVAL_DELAY']
contar=data.groupby(buscar).size()

media=np.mean(delay)
stdev=np.std(delay)
print('Media: ',media)
print('Desviacion estandar: ',stdev) 
print()
#print(contar)

l=[0,0,0,0,0,0,0]
for i in delay:
     if i>-4*stdev and i<-3*stdev:
          l[0]=l[0]+1
     if i>-3*stdev and i<-2*stdev:
          l[1]=l[1]+1
     if i>-2*stdev and i<-1*stdev:
          l[2]=l[2]+1
     if i>-1*stdev and i<stdev:
          l[3]=l[3]+1
     if i>stdev and i<2*stdev:
          l[4]=l[4]+1
     if i>2*stdev and i<3*stdev:
          l[5]=l[5]+1
     if i>3*stdev and i<4*stdev:
          l[6]=l[6]+1
n=[-4,-3,-2,-1,1,2,3,4]
for i in range(len(l)):
     print('Entre',n[i],' y ',n[i+1],': ',l[i])
cuenta, cajas, ignorar = plt.hist(delay,bins=[-4*stdev,-3*stdev,-2*stdev,-1*stdev,stdev,2*stdev,3*stdev,4*stdev])
plt.title('Distribución Normal')
plt.ylabel('Frecuencia')
plt.xlabel('Minutos de retraso')
plt.show()






#print(retrasos)
#print(statistics.stdev(data['ARRIVAL_DELAY']))