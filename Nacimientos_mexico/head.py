import csv
import pandas as pd
import sys
import os

infile = sys.argv[1]
busqueda = sys.argv[2]

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
data=pd.read_csv(infile,low_memory=True)

print(data[:int(busqueda)])

