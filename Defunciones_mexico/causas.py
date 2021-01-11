import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
from collections import Counter

infile = 'def18.csv'
buscar= 'CAUSA_DEF'
dataframe2 = 'causacsv.csv'

pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
data=pd.read_csv(infile,low_memory=True)
causa=data[buscar]
ocurrencias_causas=data.groupby(buscar).size().sort_values(ascending=False).head(25)
#print(ocurrencias_causas)

causas=['I219','E116','J189','E112','E117','K746','X954','J449','K703','E146','J440','N189','I120','I64X','C509','I110','C349','I10X','C61X','I619','E119','E142','N390','C169','E147']
descripcion=[]

#for i in range(25):
#    descripcion.append(0)
 
data2=pd.read_csv(dataframe2)
clave=data2['CLAVE']
nombre=data2['NOMBRE']

for i in range(len(clave)):
    if clave[i] == causas[0]:
        descripcion.insert(0,nombre[i])
    if clave[i] == causas[1]:
        descripcion.insert(1,nombre[i])
    if clave[i] == causas[2]:
        descripcion.insert(2,nombre[i])
    if clave[i] == causas[3]:
        descripcion.insert(3,nombre[i])
    if clave[i] == causas[4]:
        descripcion.insert(4,nombre[i])
    if clave[i] == causas[5]:
        descripcion.insert(5,nombre[i])
    if clave[i] == causas[6]:
        descripcion.insert(6,nombre[i])
    if clave[i] == causas[7]:
        descripcion.insert(7,nombre[i])
    if clave[i] == causas[8]:
        descripcion.insert(8,nombre[i])
    if clave[i] == causas[9]:
        descripcion.insert(9,nombre[i])
    if clave[i] == causas[10]:
        descripcion.insert(10,nombre[i])
    if clave[i] == causas[11]:
        descripcion.insert(11,nombre[i])
    if clave[i] == causas[12]:
        descripcion.insert(12,nombre[i])
    if clave[i] == causas[13]:
        descripcion.insert(13,nombre[i])
    if clave[i] == causas[14]:
        descripcion.insert(14,nombre[i])
    if clave[i] == causas[15]:
        descripcion.insert(15,nombre[i])
    if clave[i] == causas[16]:
        descripcion.insert(16,nombre[i])
    if clave[i] == causas[17]:
        descripcion.insert(17,nombre[i])
    if clave[i] == causas[18]:
        descripcion.insert(18,nombre[i])
    if clave[i] == causas[19]:
        descripcion.insert(19,nombre[i])
    if clave[i] == causas[20]:
        descripcion.insert(20,nombre[i])
    if clave[i] == causas[21]:
        descripcion.insert(21,nombre[i])
    if clave[i] == causas[22]:
        descripcion.insert(22,nombre[i])
    if clave[i] == causas[23]:
        descripcion.insert(23,nombre[i])
    if clave[i] == causas[24]:
        descripcion.insert(24,nombre[i])

Datas={'Causa':descripcion,
       'No. muertes':ocurrencias_causas}
df=DataFrame(Datas,columns=['Causa','No. muertes'])
#print(descripcion[0])
print(df)
#print(descripcion)
