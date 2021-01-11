import csv
import pandas as pd
from pandas import DataFrame
import sys
import os
import matplotlib.pyplot as plt
#from datetime import datetime
import datetime

infile = 'nacimientos19.csv'

pd.set_option("display.max_rows", None, "display.max_columns", None)

data=pd.read_csv(infile,low_memory=True)

fechas=data['FECH_NACH']

dias=data.groupby('FECH_NACH').size()
semanas=[]
datedias=[]
bbs=[]

for i in range(1,54):
    semanas.append(i)
    bbs.append(0)


    


for i in fechas:
    datedias.append(datetime.datetime.strptime(i, '%d/%m/%Y'))


for i in datedias:
    if i<=datetime.datetime(2019, 1, 6):
        bbs[0]=bbs[0]+1
    if i>=datetime.datetime(2019, 1, 7) and  i<=datetime.datetime(2019, 1, 13): 
        bbs[1]=bbs[1]+1
    if i>=datetime.datetime(2019, 1, 14) and  i<=datetime.datetime(2019, 1, 20): 
        bbs[2]=bbs[2]+1
    if i>=datetime.datetime(2019, 1, 21) and  i<=datetime.datetime(2019, 1, 27): 
        bbs[3]=bbs[3]+1
    if i>=datetime.datetime(2019, 1, 28) and  i<=datetime.datetime(2019, 2, 3): 
        bbs[4]=bbs[4]+1
    if i>=datetime.datetime(2019, 2, 4) and  i<=datetime.datetime(2019, 2, 10): 
        bbs[5]=bbs[5]+1
    if i>=datetime.datetime(2019, 2, 11) and  i<=datetime.datetime(2019, 2, 17): 
        bbs[6]=bbs[6]+1    
    if i>=datetime.datetime(2019, 2, 18) and  i<=datetime.datetime(2019, 2, 24): 
        bbs[7]=bbs[7]+1
    if i>=datetime.datetime(2019, 2, 25) and  i<=datetime.datetime(2019, 3, 3): 
        bbs[8]=bbs[8]+1
    if i>=datetime.datetime(2019, 3, 4) and  i<=datetime.datetime(2019, 3, 10): 
        bbs[9]=bbs[9]+1
    if i>=datetime.datetime(2019, 3, 11) and  i<=datetime.datetime(2019, 3, 17): 
        bbs[10]=bbs[10]+1
    if i>=datetime.datetime(2019, 3, 18) and  i<=datetime.datetime(2019, 3, 24): 
        bbs[11]=bbs[11]+1
    if i>=datetime.datetime(2019, 3, 25) and  i<=datetime.datetime(2019, 3, 31): 
        bbs[12]=bbs[12]+1
    if i>=datetime.datetime(2019, 4, 1) and  i<=datetime.datetime(2019, 4, 7): 
        bbs[13]=bbs[13]+1
    if i>=datetime.datetime(2019, 4, 8) and  i<=datetime.datetime(2019, 4, 14): 
        bbs[14]=bbs[14]+1
    if i>=datetime.datetime(2019, 4, 15) and  i<=datetime.datetime(2019, 4, 21): 
        bbs[15]=bbs[15]+1
    if i>=datetime.datetime(2019, 4, 22) and  i<=datetime.datetime(2019, 4, 28): 
        bbs[16]=bbs[16]+1
    if i>=datetime.datetime(2019, 4, 29) and  i<=datetime.datetime(2019, 5, 5): 
        bbs[17]=bbs[17]+1
    if i>=datetime.datetime(2019, 5, 6) and  i<=datetime.datetime(2019, 5, 12): 
        bbs[18]=bbs[18]+1
    if i>=datetime.datetime(2019, 5, 13) and  i<=datetime.datetime(2019, 5, 19): 
        bbs[19]=bbs[19]+1
    if i>=datetime.datetime(2019, 5, 20) and  i<=datetime.datetime(2019, 5, 26): 
        bbs[20]=bbs[20]+1
    if i>=datetime.datetime(2019, 5, 27) and  i<=datetime.datetime(2019, 6, 2): 
        bbs[21]=bbs[21]+1
    if i>=datetime.datetime(2019, 6, 3) and  i<=datetime.datetime(2019, 6, 9): 
        bbs[22]=bbs[22]+1
    if i>=datetime.datetime(2019, 6, 10) and  i<=datetime.datetime(2019, 6, 16): 
        bbs[23]=bbs[23]+1
    if i>=datetime.datetime(2019, 6, 17) and  i<=datetime.datetime(2019, 6, 23): 
        bbs[24]=bbs[24]+1
    if i>=datetime.datetime(2019, 6, 24) and  i<=datetime.datetime(2019, 6, 30): 
        bbs[25]=bbs[25]+1
    if i>=datetime.datetime(2019, 7, 1) and  i<=datetime.datetime(2019, 7, 7): 
        bbs[26]=bbs[26]+1
    if i>=datetime.datetime(2019, 7, 8) and  i<=datetime.datetime(2019, 7, 14): 
        bbs[27]=bbs[27]+1
    if i>=datetime.datetime(2019, 7, 15) and  i<=datetime.datetime(2019, 7, 21): 
        bbs[28]=bbs[28]+1
    if i>=datetime.datetime(2019, 7, 22) and  i<=datetime.datetime(2019, 7, 28): 
        bbs[29]=bbs[29]+1
    if i>=datetime.datetime(2019, 7, 29) and  i<=datetime.datetime(2019, 8, 4): 
        bbs[30]=bbs[30]+1
    if i>=datetime.datetime(2019, 8, 5) and  i<=datetime.datetime(2019, 8, 11): 
        bbs[31]=bbs[31]+1
    if i>=datetime.datetime(2019, 8, 12) and  i<=datetime.datetime(2019, 8, 18): 
        bbs[32]=bbs[32]+1
    if i>=datetime.datetime(2019, 8, 19) and  i<=datetime.datetime(2019, 8, 25): 
        bbs[33]=bbs[33]+1
    if i>=datetime.datetime(2019, 8, 26) and  i<=datetime.datetime(2019, 9, 1): 
        bbs[34]=bbs[34]+1
    if i>=datetime.datetime(2019, 9, 2) and  i<=datetime.datetime(2019, 9, 8): 
        bbs[35]=bbs[35]+1
    if i>=datetime.datetime(2019, 9, 9) and  i<=datetime.datetime(2019, 9, 15): 
        bbs[36]=bbs[36]+1
    if i>=datetime.datetime(2019, 9, 16) and  i<=datetime.datetime(2019, 9, 22): 
        bbs[37]=bbs[37]+1
    if i>=datetime.datetime(2019, 9, 23) and  i<=datetime.datetime(2019, 9, 29): 
        bbs[38]=bbs[38]+1
    if i>=datetime.datetime(2019, 9, 30) and  i<=datetime.datetime(2019, 10, 6): 
        bbs[39]=bbs[39]+1
    if i>=datetime.datetime(2019, 10, 7) and  i<=datetime.datetime(2019, 10, 13): 
        bbs[40]=bbs[40]+1
    if i>=datetime.datetime(2019, 10, 14) and  i<=datetime.datetime(2019, 10, 20): 
        bbs[41]=bbs[41]+1
    if i>=datetime.datetime(2019, 10, 21) and  i<=datetime.datetime(2019, 10, 27): 
        bbs[42]=bbs[42]+1
    if i>=datetime.datetime(2019, 10, 28) and  i<=datetime.datetime(2019, 11, 3): 
        bbs[43]=bbs[43]+1
    if i>=datetime.datetime(2019, 11, 4) and  i<=datetime.datetime(2019, 11, 10): 
        bbs[44]=bbs[44]+1
    if i>=datetime.datetime(2019, 11, 11) and  i<=datetime.datetime(2019, 11, 17): 
        bbs[45]=bbs[45]+1
    if i>=datetime.datetime(2019, 11, 18) and  i<=datetime.datetime(2019, 11, 24): 
        bbs[46]=bbs[46]+1
    if i>=datetime.datetime(2019, 11, 25) and  i<=datetime.datetime(2019, 12, 1): 
        bbs[47]=bbs[47]+1
    if i>=datetime.datetime(2019, 12, 2) and  i<=datetime.datetime(2019, 12, 8): 
        bbs[48]=bbs[48]+1
    if i>=datetime.datetime(2019, 12, 9) and  i<=datetime.datetime(2019, 12, 15): 
        bbs[49]=bbs[49]+1
    if i>=datetime.datetime(2019, 12, 16) and  i<=datetime.datetime(2019, 12, 22): 
        bbs[50]=bbs[50]+1
    if i>=datetime.datetime(2019, 12, 23) and  i<=datetime.datetime(2019, 12, 29): 
        bbs[51]=bbs[51]+1
    if i>=datetime.datetime(2019, 12, 30) and  i<=datetime.datetime(2019, 12, 31): 
        bbs[52]=bbs[52]+1

for i in range(len(bbs)):
    print('semana:',semanas[i],' ',bbs[i])

Datas={'Semanas':semanas,
       'Nacimientos':bbs}
df=DataFrame(Datas,columns=['Semanas','Nacimientos'])
df.plot(x='Semanas',y='Nacimientos',kind='bar')
plt.show()