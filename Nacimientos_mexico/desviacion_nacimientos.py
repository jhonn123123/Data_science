import pandas as pd
import numpy as np
import csv
import math
import sys
import os
import statistics

infile = sys.argv[1]


pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)

talla=data['TALLAH']
peso=data['PESOH']
TT=talla.sum()
TP=peso.sum()
maximoT=talla.max()
maximoP=peso.max()
minimoT=talla.min()
minimoP=peso.min()
desviacionT=0
desviacionP=0
suma=0
suma2=0

mediaT=TT/len(talla)
mediaP=TP/len(peso)

"""for i in range(len(talla)):
    xuT=(i-mediaT)**2
    xuP=(i-mediaP)**2
    suma=suma+xuT
    suma2=suma2+xuP

desviacionT=math.sqrt(suma/len(talla))
desviacionP=math.sqrt(suma2/len(peso))"""

print()
print('Promedio Talla: \t',mediaT,'cm')
#print('stdev Talla: ', desviacionT)
print('stdev Talla: \t\t', statistics.stdev(talla),'cm')
print('Minimo Talla: \t\t',minimoT,'cm')
print('Maximo Talla : \t\t',maximoT,'cm')
print('n: \t\t\t',len(talla))

print('\nPromedio Peso: \t\t',mediaP/1000,'kg')
#print('stdev Peso: ',desviacionP)
print('stdev Peso: \t\t',statistics.stdev(peso)/1000,'kg')
print('Minimo Peso: \t\t',minimoP/1000,'kg')
print('Maximo Peso : \t\t',maximoP/1000,'kg')
print('n: \t\t\t',len(peso))


