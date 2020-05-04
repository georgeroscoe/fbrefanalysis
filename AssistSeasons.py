#!python3
import pandas as pd
import csv
from collections import Counter

df = pd.read_csv('ALLData2.csv',sep=',',encoding="utf8")


df2 = df.sort_values(by=['player','season'])

lst = []

for index, row in df.iterrows():

    if (df['A'].loc[index] > 9):
            lst.append((df['player'].loc[index], int(df['A'].loc[index]), df['season'].loc[index]))

lst.sort(key=lambda tup: tup[1],reverse=True)

cnt = Counter(elem[0] for elem in lst).most_common(15)

fields = ['player', 'Number of 10+ assist seasons']

rows = cnt

with open('AssistSeasons.csv','w', encoding="utf-8") as  csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
