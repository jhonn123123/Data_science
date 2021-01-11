import pandas as pd
from pandas import DataFrame
import sys
import os
from ast import literal_eval
import gzip
import json 
import csv 
from pandas.io.json import json_normalize

pd.set_option("display.max_rows", None, "display.max_columns", None)
path='Video_Games.json.gz'

def parse(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield json.loads(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('Video_Games.json.gz')
df.to_csv('games.csv')
#print(df)

"""ratings = []
verified=[]
reviewTime=[]
reviewerID=[]
asin=[]
reviewerName=[]
reviewText=[]
summary=[]
unixReviewTime=[]

for review in parse("Video_Games.json.gz"):
  ratings.append(review['overall'])
  verified.append(review['verified'])
  reviewTime.append(review['reviewTime'])
  reviewerID.append(review['reviewerID'])
  asin.append(review['asin'])
  reviewerName.append(review['reviewerName'])
  reviewText.append(review['reviewText'])
  summary.append(review['summary'])
  unixReviewTime.append(review['unixReviewTime'])
  #lengreviewText.append(len(review['reviewText']))
  #lensummary.append(len(review['summary']))

Datas={'ID':reviewerID,
       'Name':reviewerName,
       'Rating':ratings,
       'Asin':asin,
       'Review':reviewText,
       'Summary':summary,
       'Verified':verified,
       'ReviewTime':reviewTime,
       'Unix':unixReviewTime}

df=DataFrame(Datas,columns=['ID','Name','Rating','Asin','Review','Summary','Verified','ReviewTime','Unix'])
df.to_csv('videogames.csv',chunksize=1000000)"""
#print(df)
#print (sum(ratings) / len(ratings))



