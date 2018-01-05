import numpy as np
import pandas as pd
import os
import json

list_file = []
for file in os.listdir('./departs_arrives'):
    filename = os.fsdecode(file) 
    list_file.append(os.path.join(filename).split('_')[2].split('.')[0])

list_file = list(set(list_file))
print(len(list_file))

import csv
dates = [2010,2011,2012,2013,2014,2015,2016,2017]
d = {}
dep_ar = ['ARR','DEP']
for item in list_file:
    d[item]={}
    for elt in dep_ar: 
        with open('./departs_arrives/Vols_'+elt+'_'+item+'.csv', 'r') as df:
            try:
                next(df)
            except StopIteration:
                continue
            i=8
            reader = csv.reader(df)
            d[item][elt]={}
            for date in dates:
                d[item][elt][date]={}
                for row in reader:
                    d[item][elt][date][row[0]]=row[i]
                i-=1

with open('data.json', 'w') as fp:
    json.dump(d, fp)