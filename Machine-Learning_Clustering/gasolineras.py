import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
k=int(input('Numero de clusters: '))

infile = 'latlong.csv'
longi= 'long'
lat='lat'
pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
data=pd.read_csv(infile,low_memory=True)
data.columns=['long','lat']
longitud=data[longi]
latitud=data[lat]

plt.scatter(longitud,latitud,cmap='rainbow')
#plt.show()

kmeans = KMeans(n_clusters=k).fit(data)
centroids = kmeans.cluster_centers_
#print(centroids)
plt.scatter(longitud, latitud, c= kmeans.labels_.astype(float),cmap='rainbow', s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50,)

plt.show()