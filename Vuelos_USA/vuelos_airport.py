import pandas as pd
from pandas import DataFrame
import sys
import os

infile = 'flights.csv'
buscar = 'ORIGIN_AIRPORT'
buscar2 = 'DESTINATION_AIRPORT'

pd.set_option("display.max_rows", None, "display.max_columns", None)

data=pd.read_csv(infile,low_memory=True)
Datas={'ORIGIN_PORT':data.groupby(buscar).size(),'DESTINATION_PORT':data.groupby(buscar2).size()}
df=DataFrame(Datas,columns=['ORIGIN_PORT','DESTINATION_PORT'])
#print(data.groupby(buscar).size())
#print(df)
print(df['DESTINATION_PORT'])