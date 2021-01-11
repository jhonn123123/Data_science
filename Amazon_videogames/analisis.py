import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
#-100.406013, 20.593278 itq
infile = 'games.csv'
pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile)

#print(data['overall'])

name=data['reviewerName']
rating=data['overall']
review=data['reviewText'].astype(str)
summary=data['summary'].astype(str)
lenreview=[]
lensummary=[]

for i in review:
    lenreview.append(len(i))

for i in summary:
    lensummary.append(len(i))

Amazon={'Nombre':name,
        'Rating':rating,
        'Long_Review':lenreview,
        'Long_Summary':lensummary}

df=DataFrame(Amazon,columns=['Nombre','Rating','Long_Review','Long_Summary'])

#print(df)
print('Numero de calificaciones por estrellas ordenado de mayor a menor')
filtro1=df.groupby('Rating').size().sort_values(ascending=False)
print(filtro1)
print()
filtro2=df.groupby('Rating').mean()["Long_Review"].sort_values(ascending=False)
print('Promedio de Numero de letras de comentarios por calificaciones de 1 a 5 ordenado de mayor a menor')
print(filtro2)
print()
filtro3=df.groupby('Rating').mean()["Long_Summary"].sort_values(ascending=False)
print('Promedio de Numero de letras de Summary por calificaciones de 1 a 5 ordenado de mayor a menor')
print(filtro3)



