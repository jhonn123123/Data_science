import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as CM
from matplotlib import mlab as ML




infile = '/home/jhonn/Documentos/ciencia_datos/Machine-Learning_Clustering/latlong.csv'
longi= 'long'
lat='lat'
pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
data=pd.read_csv(infile,low_memory=True)
data.columns=['long','lat']
longitud=data[longi]
latitud=data[lat]

"""plt.scatter(longitud,latitud,cmap='plasma')
plt.show()"""
x=longitud
y=latitud

heatmap, xedges, yedges = np.histogram2d(x, y, bins=30)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.imshow(heatmap.T, extent=extent, origin='lower')
plt.show()