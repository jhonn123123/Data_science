import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
import random
import pandas as pd
from sklearn.cluster import KMeans


#plt.figure(figsize=(12, 12))
n=int(input('Numero de puntos: '))
k=int(input('Numero de clusters: '))

x=[]
y=[]

for i in range(n):
    x.append(random.randint(0,1000))
    y.append(random.randint(0,1000))

df=pd.DataFrame({'x':x,'y':y})
kmeans = KMeans(n_clusters=k).fit(df)
centroids = kmeans.cluster_centers_
#print(centroids)
plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float),cmap='rainbow', s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()
