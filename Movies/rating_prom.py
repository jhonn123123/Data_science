import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
from datetime import datetime
from time import time

infile = 'ratings.csv'
buscar= 'movieId'
infile2 = 'movies.csv'
buscar2= 'title'
r=sys.argv[1]
start_time = time()

pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
data=pd.read_csv(infile,low_memory=True)

movie=data[buscar]
data2=pd.read_csv(infile2,low_memory=True)
movieid=data2[buscar]
rating=[]
hora=[]
n=[]
peliculas=data2[buscar2]
fecha_min=[]

for i in range(len(movieid)):
       rating.append(np.mean(data[data[buscar]==i+1].rating))
       n.append(len(data[data[buscar]==i+1].rating))
       fecha_min.append(np.min(data[data[buscar]==i+1].timestamp.astype("Float32").astype("Int32")))

Datas={'Movies':peliculas,
       'Rating avg':rating,
       'Num_evaluaciones':n,
       'Fecha_min': fecha_min}
df=DataFrame(Datas,columns=['Movies','Num_evaluaciones','Rating avg','Fecha_min'])
print(df[df['Rating avg']>=float(r)])

tiempo = time() - start_time
minutos=tiempo/60
segundos=tiempo%60
print()
print('tiempo de ejecución: ',int(minutos),'.',segundos,'minutos')