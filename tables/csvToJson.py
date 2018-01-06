import numpy as np
import pandas as pd
import os
import json

list_file = []
for file in os.listdir('./departs_arrives'):
    filename = os.fsdecode(file) 
    list_file.append(os.path.join(filename).split('_')[2].split('.')[0])

list_file = list(set(list_file))

import csv
dates = [2010,2011,2012,2013,2014,2015,2016,2017]
d = {}
dep_ar = ['ARR','DEP']

code_to_country = {}
with open('coutry_code.csv', 'r') as c:
    data = csv.reader(c)
    for row in c:
        row = row.split(',')
        code_to_country[row[2]] = row[4]

list_pays = []
for item in list_file:
    pays=code_to_country[item]
    list_pays.append(pays)
    d[pays]={}
    for elt in dep_ar:
        d[pays][elt]={}
        i=8
        for date in dates:
            d[pays][elt][date]={}
            with open('./departs_arrives/Vols_'+elt+'_'+item+'.csv', 'r') as df:
                try:
                    next(df)
                except StopIteration:
                    continue
                reader = csv.reader(df)
                for row in reader:
                    d[pays][elt][date][row[0]]=row[i]
                i-=1

print(list_pays)
with open('data.json', 'w') as fp:
    json.dump(d, fp)