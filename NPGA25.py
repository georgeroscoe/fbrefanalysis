#!python3
import pandas as pd
import csv

df = pd.read_csv('ALLData2.csv',sep=',',encoding="utf8")


lst = []

for index, row in df.iterrows():

    if  df['NPGA'].loc[index] > 24:
            lst.append((df['player'].loc[index], df['NPGA'].loc[index], df['season'].loc[index]))


lst.sort(key=lambda tup: tup[1],reverse=True)

fields = ['player', 'NPGA', 'season']

rows = lst

with open('NPGA25.csv','w', encoding="utf-8") as  csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
