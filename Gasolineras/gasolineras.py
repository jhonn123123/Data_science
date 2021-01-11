import pandas as pd
from pandas import DataFrame
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as et 
#import pandas_read_xml as pdx

pd.set_option("display.max_rows", None, "display.max_columns", None,'display.width', None,'display.max_colwidth', None)
xml1='places.xml'
xml2='prices.xml'

parsedXML = et.parse(xml1)
dfcols = ['id','name','longitud','latitud']
#dfcols = ['id','name','longitud','latitud','regular','premium','diesel']
df = pd.DataFrame(columns=dfcols)
def getvalueofnode( node ):
    return node.text if node is not None else None
for node in parsedXML.getroot():
    ids=node.attrib.get('place_id')
    name=node.find('name')
    x=node.find('location/x')
    y=node.find('location/y')
    df = df.append( pd.Series( 
    [ids,getvalueofnode(name),getvalueofnode(x),getvalueofnode(y)],index=dfcols),ignore_index=True)

#print(df)

parsedXML = et.parse(xml2)
dgcols = ['id','regular','premium','diesel']
#dfcols = ['id','name','longitud','latitud','regular','premium','diesel']
dg = pd.DataFrame(columns=dgcols)
def getvalueofnode( node ):
    return node.text if node is not None else None
for node in parsedXML.getroot():
    ids=node.attrib.get('place_id')
    #if node.get('type') == 'regular' ||  node.get('type') == 'regular'
    regular=node.find('gas_price[@type="regular"]')
    premium=node.find('gas_price[@type="premium"]')
    diesel=node.find('gas_price[@type="diesel"]')
    dg = dg.append( pd.Series( 
    [ids,getvalueofnode(regular),getvalueofnode(premium),getvalueofnode(diesel)],index=dgcols),ignore_index=True)

df=df.drop_duplicates(['id'],keep='last')
dg=dg.drop_duplicates(['id'],keep='last')
df.set_index('id', inplace = True)
dg.set_index('id', inplace = True)

#print(df.head(100))
#print(dg.head(100))

gg=pd.concat([df,dg],axis=1)
print(gg)
gg.to_csv('gasolineras.csv')

"""
idss=dg['id'].sort_index().drop_duplicates()
names=df['name'].sort_index()
x=df['longitud'].sort_index()
y=df['latitud'].sort_index()
r=dg['regular'].sort_index()
p=dg['premium'].sort_index()
d=dg['diesel'].sort_index()
Datas={'id':idss,'name':names,'longitud':x,'latitud':y,'regular':r,'premium':p,'diesel':d}
gg=DataFrame(Datas,columns=['id','name','longitud','latitud','regular','premium','diesel'])
print(gg)"""




"""
xtree =et.parse(xml1)
xroot=xtree.getroot()
#xroot2=xtree.get('location')

df_cols=['id','name','longitud','latitud']
rows=[]

for node in xroot:
    s_id=node.attrib.get('place_id') 
    name=node.find('name').text if node is not None else None
    cre_id=node.find('cre_id').text if node is not None else None
    
    location=node.attrib.get('location')
    x=node.find('x').text if node is not None else None
    y=node.find('y').text if node is not None else None
    rows.append({'id':s_id,'name':name})

out_df=pd.DataFrame(rows,columns=df_cols)

print(out_df)
"""
