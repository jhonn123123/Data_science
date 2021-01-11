import pandas as pd
from pandas import DataFrame
import sys
import os

infile = 'flights.csv'
buscar = 'ORIGIN_AIRPORT'
buscar2 = sys.argv[1]

pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)
origen=data[buscar]

filtro=data[data[buscar]==buscar2]['DESTINATION_AIRPORT']

print('Vuelos totales: ',filtro.count())
print()
contars=data.groupby(filtro).size()
print(contars.sort_values(ascending=False))
