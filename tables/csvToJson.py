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
        d[item][elt]={}
        i=8
        for date in dates:
            d[item][elt][date]={}
            with open('./departs_arrives/Vols_'+elt+'_'+item+'.csv', 'r') as df:
                try:
                    next(df)
                except StopIteration:
                    continue
                reader = csv.reader(df)
                for row in reader:
                    print(date)
                    d[item][elt][date][row[0]]=row[i]
                i-=1

with open('data.json', 'w') as fp:
    json.dump(d, fp)