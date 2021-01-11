import pandas as pd
from pandas import DataFrame
import numpy as np
import sys
import os
import statistics
import matplotlib.pyplot as plt 
from scipy import stats
#from mpl_toolkits.mplot3d import Axes3D
#from matplotlib import cm
#from sklearn import linear_model
from sklearn.linear_model import LinearRegression 

infile = sys.argv[1]
buscar = sys.argv[2]
buscar2 = sys.argv[3]

pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)
#y=bX+a
x=data[buscar]
y=data[buscar2]
n=len(x)

Ex=x.sum()
Ey=y.sum()
Exy=(x*y).sum()
Ex2=(x*x).sum()
Ey2=(y*y).sum()

b=((n*Exy)-Ex*Ey)/((n*Ex2)-(Ex*Ex))
a=((Ex2+Ey)-(Exy*Ex))/((n*Ex2)-(Ex*Ex))
Sxx=Ex2-((Ex*Ex)/n)
Syy=Ey2-((Ey*Ey)/n)
Sxy=Exy-((Ex*Ey)/n)
r=Sxy/np.sqrt(Sxx*Syy)

def f(x):  
    y = b*x + a 
    return y
y = f(x)
plt.scatter(x,y,label='data', color='blue')
plt.title('Datos');
plt.show()

#plt.scatter(x, y)
#plt.show()


