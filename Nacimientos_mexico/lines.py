import csv
import pandas as pd
import sys
import os

infile = sys.argv[1]
n = sys.argv[2]
m = sys.argv[3]

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
#pd.set_option('display.width',1000)

data=pd.read_csv(infile,low_memory=True)

print(data[int(n):int(m)])