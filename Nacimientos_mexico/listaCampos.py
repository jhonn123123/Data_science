import csv
import pandas as pd
import sys
import os

infile = sys.argv[1]

data=pd.read_csv(infile)
i=0
for col in data.columns:
    print(i,' ',col)
    i+=1   