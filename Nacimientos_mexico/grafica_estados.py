import csv
import pandas as pd
from pandas import DataFrame
import sys
import os
import matplotlib.pyplot as plt

infile = 'nacimientos19.csv'
buscar = 'CEDOCVE'

pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)
estados=['Aguascalientes','Baja California','Baja California Sur','Campeche','Coahuila','Colima','Chiapas','Chihuahua','Ciudad de Mexico','Durango','Guanajuato','Guerrero','Hidalgo','Jalisco','Mexico','Michoacan','Morelos','Nayarit','Nuevo Leon','Oaxaca','Puebla','Queretaro','Quintana Roo','San Luis Potosi','Sinaloa','Sonora','Tabasco','Tamaulipas','Tlaxcala','Veracruz','Yucatan','Zacatecas']
nacimientos=[]
values=data.groupby(buscar).size()

Datas={'Estados':estados,
       'Nacimientos':values}
df=DataFrame(Datas,columns=['Estados','Nacimientos'])
df.plot(x='Estados',y='Nacimientos',kind='bar')
#plt.savefig('estados.png')


print(df)       
       

plt.show()


#ax=values.plot.bar(x='estados',y='nacimientos',rot=0)
#plt.show()
#print(datos)