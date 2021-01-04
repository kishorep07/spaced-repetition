import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from datetime import datetime, timedelta
import json
import boto3

file = 'LC.xlsm'
date_col = 'Unnamed: 0'
df = pd.read_excel(file)
client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb', region_name = 'ap-south-1')
table = dynamodb.Table('lc-tracker')

cnt = 0
schedule = {}
for i in range(2, len(df), 2):
    if type(df[date_col][i]) is float: continue
    date = df[date_col][i]
    if date >= date.today(): break
    date = date.strftime('%x')
    schedule[date] = {
        'day': cnt,
        'date': date,
        'status' : 1,
        'qs' : []
    }

    for index in df.columns.values[3:]:
        if type(df[index][i]) is str and df[index][i] != 'nan':
            schedule[date]['qs'].append(df[index][i])
    
    cnt += 1

#or d in schedule: print (d, schedule[d])
#print(json.dumps(schedule, indent = 4))
# # 1, 3, 7 -> 7, 21, 49
for d in schedule:table.put_item(Item = schedule[d])