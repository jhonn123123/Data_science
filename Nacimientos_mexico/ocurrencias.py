import csv
import pandas as pd
import sys
import os

infile = sys.argv[1]
buscar = sys.argv[2]

pd.set_option("display.max_rows", None, "display.max_columns", None)
#pd.set_option('display.max_rows',500)
#pd.set_option('display.max_columns',500)



data=pd.read_csv(infile,low_memory=True)
#print(data[buscar].value_counts(dropna=False).fillna(0))
print(data.groupby(buscar).size())