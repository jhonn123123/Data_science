import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np

infile = 'def18.csv'
buscar= 'SEXO'
buscar2='ENT_OCURR'
infile2 = '/home/jhonn/Documentos/ciencia_datos/nacimientos/nacimientos19.csv'

pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
data=pd.read_csv(infile,low_memory=True)
genero=data[buscar]
hombres=0
mujeres=0
NE=0
nM=len(genero)
for i in genero:
    if i == 1:
        hombres+=1
    if i == 2:
        mujeres+=1
    if i==9:
        NE+=1

print('Hombres: ',hombres)
print('Mujeres: ',mujeres)
print('No especificado: ',NE)
print()
estados=['Aguascalientes','Baja California','Baja California Sur','Campeche','Coahuila','Colima','Chiapas','Chihuahua','Ciudad de Mexico','Durango','Guanajuato','Guerrero','Hidalgo','Jalisco','Mexico','Michoacan','Morelos','Nayarit','Nuevo Leon','Oaxaca','Puebla','Queretaro','Quintana Roo','San Luis Potosi','Sinaloa','Sonora','Tabasco','Tamaulipas','Tlaxcala','Veracruz','Yucatan','Zacatecas','NE']
totalEstado=[1312544,3315766,712029,899931,2954915,711235,5217908,3556574,8918653,1754754,5853677,3533251,2858359,7844830,16187608,4584471,1903811,1181050,5119504,3967889,6168883,2038372,1501562,2717820,2966321,2850330,2395272,3441698,1272847,8112505,2097175,1579209,1]
porcentaje=[]
values=data.groupby(buscar2).size()

Datas={'Estados':estados,
       'Muertes':values}
muertes=Datas['Muertes']
j=0
for i in muertes:
    porcentaje.append(i*100/totalEstado[j])
    j+=1
Datas={'Estados':estados,
       'Muertes':values,
       'o/o Poblacion Total':porcentaje}
df=DataFrame(Datas,columns=['Estados','Muertes','o/o Poblacion Total'])
#print(df)
print()
data2=pd.read_csv(infile2,low_memory=True)
nN=len(data2['CEDOCVE'])
print('No. de Muertos 2018: ',nM)
print('No. de Nacimientos 2019: ',nN)
nacimientos_estados=data2.groupby('CEDOCVE').size()
f=nacimientos_estados-values
    
#print(f)

Datas={'Estados':estados,
       'Muertes':values,
       'o/o Poblacion Total':porcentaje,
       'Nacimientos 2019':nacimientos_estados,
       'Nacimientos - Muertes':f}
df=DataFrame(Datas,columns=['Estados','Muertes','o/o Poblacion Total','Nacimientos 2019','Nacimientos - Muertes'])
print(df)