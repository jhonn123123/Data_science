#EDAD
import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np

infile = 'def18.csv'
buscar= 'EDAD'

pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)
muertes=data[buscar]
horas=0
dias=0
meses=0
años=0
anio=[]
for i in muertes:
    if i>1000 and i<2000:
       horas+=1 
    if i>2000 and i<3000:
        dias+=1
    if i>3000 and i<4000:
        meses+=1
    if i>4000 and i<4998:
        años+=1
        anio.append(i-4000)

print('Horas: \t',horas)
print('Dias: \t',dias)
print('Meses: \t',meses)
print('Años: \t',años)
media=0
for i in anio:
    media+=i
media=media/len(anio)
print('Media de edad de muertes: \t',media)
lustros=[]
for i in range (24):
    lustros.append(0)
for i in anio:
    if i>=0 and i<5:
        lustros[0]=lustros[0]+1
    if i>=5 and i<10:
        lustros[1]=lustros[1]+1
    if i>=10 and i<15:
        lustros[2]=lustros[2]+1
    if i>=15 and i<20:
        lustros[3]=lustros[3]+1
    if i>=20 and i<25:
        lustros[4]=lustros[4]+1
    if i>=25 and i<30:
        lustros[5]=lustros[5]+1
    if i>=30 and i<35:
        lustros[6]=lustros[6]+1
    if i>=35 and i<40:
        lustros[7]=lustros[7]+1
    if i>=40 and i<45:
        lustros[8]=lustros[8]+1
    if i>=45 and i<50:
        lustros[9]=lustros[9]+1
    if i>=50 and i<55:
        lustros[10]=lustros[10]+1
    if i>=55 and i<60:
        lustros[11]=lustros[11]+1
    if i>=60 and i<65:
        lustros[12]=lustros[12]+1
    if i>=65 and i<70:
        lustros[13]=lustros[13]+1
    if i>=70 and i<75:
        lustros[14]=lustros[14]+1
    if i>=75 and i<80:
        lustros[15]=lustros[15]+1
    if i>=80 and i<85:
        lustros[16]=lustros[16]+1
    if i>=85 and i<90:
        lustros[17]=lustros[17]+1
    if i>=90 and i<95:
        lustros[18]=lustros[18]+1
    if i>=95 and i<100:
        lustros[19]=lustros[19]+1
    if i>=100 and i<105:
        lustros[20]=lustros[20]+1
    if i>=105 and i<110:
        lustros[21]=lustros[21]+1
    if i>=110 and i<115:
        lustros[22]=lustros[22]+1
    if i>=115 and i<120:
        lustros[23]=lustros[23]+1
j=0
for i in range(0,24):
    print('Lustro de ',j,' a ',end='')
    j+=5
    print(j,' años: ', lustros[i])