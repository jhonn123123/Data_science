import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np

infile = 'movies.csv'
buscar= 'title'

pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)

peliculas=data[buscar]
generos=['Action','Adventure','Animation',"Children",'Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western','no genres listed']
ngeneros=[]
print('Numero de peliculas: ',len(peliculas))
dosmil=data[peliculas.str.contains('(2000)',case=False)]
print('Peliculas del 2000: ',len(dosmil))
print()
for i in generos:
    ngeneros.append(len(data[data['genres'].str.contains(i,case=False)]))
#genero=data.groupby('genres').size()
Datas={'Generos':generos,
       'Cantidad':ngeneros}
df=DataFrame(Datas,columns=['Generos','Cantidad'])

print(df.loc[df['Cantidad'].idxmax(),:])
print()
#for i in peliculas:
#    if i

