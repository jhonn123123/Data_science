import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

infile='netflix.csv'

pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
data=pd.read_csv(infile)

pais=data['country']
tipe=data['type']
tipos=data.groupby('type').size()
paises=data.groupby('country').size()
npaises=data['country'].drop_duplicates()
anno=data.groupby('date_added').size()


countrys=['Argentina','Australia','Austria','Armenia','Bangladesh','Belgium','Brazil','Bulgaria','Cambodia','Canada','Chile','China','Colombia','Croatia','Cyprus','Czech Republic','Denmark','Dominican Republic','Egypt','Finland','France','Georgia','Germany','Ghana','Guatemala','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Ireland','Israel','Italy','Japan','Lebanon','Malaysia','Mauritius','Mexico','Netherlands','New Zealand','Nigeria','Norway','Pakistan','Paraguay','Peru','Philippines','Poland','Portugal','Romania','Russia','Saudi Arabia','Serbia','Singapore','Slovenia','Somalia','South Africa','South Korea','Soviet Union','Spain','Sweden','Switzerland','Syria','Taiwan','Thailand','Turkey','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Venezuela','Vietnam','West Germany']
ppaises=[]
#print(npaises.sort_values())

for i in countrys:
    ppaises.append(len(data[data['country'].str.contains(i,na=False)]))

Datas={'Paises':countrys,'Producciones':ppaises}
df=DataFrame(Datas,columns=['Paises','Producciones'])
#print(df)
#df.plot(x='Paises',y='Producciones',kind='bar')
#plt.show()
y=[]
for i in range(2011,2020):
    y.append(i)
anios=[]
movies=[]
series=[]

j=2011

for i in range(2011,2020):
    print(i)
    peliculas=data[data['date_added'].str.contains(str(i),na=False)][['date_added','type']]
    print('Peliculas: ',sum(peliculas['type']=='Movie'))
    print('Series: ',sum(peliculas['type']=='TV Show'))
    print()
"""for i in range(2011,2020):
    anios.append(len(data[data['date_added'].str.contains(str(i),na=False)]))
#print(anios)
Years={'Año':y,'Producciones':anios}
df=DataFrame(Years,columns=['Año','Producciones'])
print(df)"""

minutes=[]
tmin=0.0
movies=data[data['type']=='Movie'][['type','duration']]
series=data[data['type']=='TV Show'][['type','duration']]
temporadas=[]
ttemporadas=0
#print(movies['duration'])

for i in movies['duration']:
    minutes=i.split()
    tmin=tmin+int(minutes[0])

for i in series['duration']:
    temporadas=i.split()
    ttemporadas+=int(temporadas[0])
    #print(temporadas)
    
print("Total de minutos en peliculas: ",tmin)
print("Total de Temporadas en Series: ",ttemporadas)

    

    




    
