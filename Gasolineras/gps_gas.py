import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
#-100.406013, 20.593278 itq
infile = 'gasolineras.csv'
longituditq=-100.406013
latituditq=20.593278
pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
data=pd.read_csv(infile)
#updata=data.drop([7024,23393])
#print(updata.head(200))

longitud=data['longitud']
latitud=data['latitud']
name=data['name']
regular=data['regular']
premium=data['premium']
diesel=data['diesel']

def neer(longituditq,latituditq,name,regular,premium,diesel,data,longitud,latitud):
    print('longitud: ',longituditq)
    print('latitud: ',latituditq)
    print()
    k=10
    rla=(1*k)/111.12
    rlo=(1*k)/111.32
    filtro=((latitud >= latituditq)&(latitud<=latituditq+rla))|((latitud <= latituditq)&(latitud>=latituditq-rla)) 
    filtro2=((longitud >= longituditq)&(longitud<=longituditq+rlo))|((longitud <= longituditq)&(longitud>=longituditq-rlo)) 
    #filtro=((latitud >= latituditq)&(latitud<=latituditq+rla))|((latitud <= latituditq)&(latitud>=latituditq-rla)) & ((longitud >= longituditq)&(longitud<=longituditq+rlo))|((longitud <= longituditq)&(longitud>=longituditq-rlo)) 
    #gas_cerca=data[(latitud >= latituditq)&(latitud<=latituditq+rla)]
    gas_cerca=data[filtro&filtro2]
    print(gas_cerca.sort_values(by='regular'))
    plt.scatter(gas_cerca['longitud'],gas_cerca['latitud'],cmap='rainbow')
    
    plt.scatter(longituditq,latituditq,color='r')
    plt.show()

neer(longituditq,latituditq,name,regular,premium,diesel,data,longitud,latitud)


"""plt.scatter(longitud,latitud,cmap='rainbow')
plt.show()"""
