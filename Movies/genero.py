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
generos=['Action','Adventure','Animation',"Children",'Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western','no genres listed']
start_time = time()

pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
data=pd.read_csv(infile,low_memory=True)

movie=data[buscar]
data2=pd.read_csv(infile2,low_memory=True)
movieid=data2[buscar]
rating=[]
peliculas=data2[buscar2]
ngeneros=data2['genres']


rgeneros=[]
for i in range(len(movieid)):
       rating.append(np.mean(data[data[buscar]==i+1].rating))

Datas={'Movies':peliculas,
       'Genero':ngeneros,
       'Rating avg':rating}

df=DataFrame(Datas,columns=['Movies','Genero','Rating avg'])


#for i in generos:
for i in range(len(generos)):
    #print(df[df['Genero']==generos[i]].sort_values(by='Rating avg',ascending=False).head(10))
    print(df[df['Genero']==generos[i]].sort_values(by='Rating avg',ascending=False).head(10))
    print()
    #ngeneros.append(len(data2[data2['genres'].str.contains(i,case=False)]))
tiempo = time() - start_time
minutos=tiempo/60
segundos=tiempo%60
print()
print('tiempo de ejecución: ',int(minutos),'.',segundos,'minutos')