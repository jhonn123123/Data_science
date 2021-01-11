import pandas as pd
from pandas import DataFrame
import numpy as np
import sys
import os
import statistics
import matplotlib.pyplot as plt 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model

infile='gdp.csv'

pd.set_option("display.max_rows", None, "display.max_columns", None)
data=pd.read_csv(infile,low_memory=True)
x=data['Entity']
y=data['GDP']
year=data['Year']

buscar=input('Pais: ')

filtro=data[data['Entity']==buscar]['GDP']#gdp  (y)
filtro2=data[data['Entity']==buscar]['Year'] #(x)
#print(filtro2)

plt.bar(filtro2,filtro,color='c')
plt.title(buscar)
plt.show()
#filtro2=df.groupby('Rating').mean()["Long_Review"].sort_values(ascending=False)
#print('Promedio de Numero de letras de comentarios por calificaciones de 1 a 5 ordenado de mayor a menor')
buscar2=int(input('Año: '))
filtro3=data[data['Year']==buscar2][['Entity','GDP']].sort_values(by='GDP',ascending=False) 
print(filtro3)



data=pd.read_csv('2019.csv',low_memory=True)


def estimate_coef(x, y):
    n=np.size(x)
    m_x, m_y = np.mean(x), np.mean(y) 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 

    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 

    return(b_0, b_1) 

def plot_regression_line(x, y, b): 
    plt.scatter(x, y, color = "c", marker = "o", s = 30) 
    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = "r")
    plt.title('2019')
    plt.xlabel('Paises') 
    plt.ylabel('Felicidad') 
    plt.show()

def main(): 
    x=data['Score']
    #y=data['GDP per capita']
    y=data['Overall rank']
    #y=data['Country or region']
    n=len(x)
    b = estimate_coef(x, y)
    plot_regression_line(x, y, b)

main()


  