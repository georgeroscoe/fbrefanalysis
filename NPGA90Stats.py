#!python3
import pandas as pd
import csv

df = pd.read_csv('ALLData2.csv',sep=',',encoding="utf8")

lst = []

for index, row in df.iterrows():

    if (df['NPGA/90'].loc[index] > 0.9) & (df['minutes'].loc[index] > 1500):
            lst.append((df['player'].loc[index], df['NPGA/90'].loc[index], df['season'].loc[index], int(df['minutes'].loc[index])))

lst.sort(key=lambda tup: tup[1],reverse=True)

fields = ['player', 'NPGA/90','season','minutes']

rows = lst

with open('NPGA90Stats.csv','w', encoding="utf-8") as  csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
