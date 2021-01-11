import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
from datetime import datetime
from time import time

start_time = time()
infile = 'ratings.csv'
buscar= 'movieId'
infile2 = 'movies.csv'
buscar2= 'title'

pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)

movie=data[buscar]
data2=pd.read_csv(infile2,low_memory=True)
movieid=data2[buscar]
rating=[]
hora=[]
n=[]
peliculas=data2[buscar2]
fecha_min=[]
fecha_max=[]

#filtro=data[data[buscar]==1]
for i in range(len(movieid)):
       rating.append(np.mean(data[data[buscar]==i+1].rating))
       n.append(len(data[data[buscar]==i+1].rating))
       #fmin=datetime.fromtimestamp(data[data[buscar]==i+1].timestamp)
       #fmax=datetime.fromtimestamp(data[data[buscar]==i+1].timestamp)
       fecha_min.append(np.min(data[data[buscar]==i+1].timestamp.astype("Float32").astype("Int32")))
       fecha_max.append(np.max(data[data[buscar]==i+1].timestamp.astype("Float32").astype("Int32")))
       #rating.append(data[data[buscar]==i].rating.mean())

Datas={'Movies':peliculas,
       'Rating avg':rating,
       'Num_evaluaciones':n,
       'Fecha_min': fecha_min,
       'Fecha_max':fecha_max}
df=DataFrame(Datas,columns=['Movies','Rating avg','Num_evaluaciones','Fecha_min','Fecha_max'])
print(df)
tiempo = time() - start_time
minutos=tiempo/60
segundos=tiempo%60

print()
print('tiempo de ejecución: ',int(minutos),'.',segundos,'minutos')


#print(rating[296])
#for i in range(len(movie)):
 