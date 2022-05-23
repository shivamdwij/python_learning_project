from audioop import add
import dis
from os import stat
from threading import local
import requests
import json
import pandas as pd
import csv

import json

def datapush(name,lat,lon,address,locality,city,id,state,phone_number):
  url = "http://10.140.0.204:80/dedupe"
  payload = json.dumps({
    "name": str(name),
    "lat": lat,
    "lon": lon,
    "address": str(address),
    "locality": str(locality),
    "city": str(city),
    "id": str(id),
    "state": str(state),
    "phone_number": str(phone_number)
  })
  headers = {
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  response = json.loads(response.text)

  return response

data = pd.read_csv('/home/analytics/venv/Analytics/Discovery_Analytics/data.csv',encoding='latin-1')

data = data.values.tolist()

final_data = []

for i in data:

  response = datapush(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
  print(response)
  final = []
  id_data = response['id']
  merchant_ids = response['merchant_ids']
  try:
    merchant_ids = merchant_ids[0]
  except:
    merchant_ids = 0
  changed_mappings = response['changed_mappings']
  status = response['status']
  try:
    name_score = response['scores']['name_score']
  except:
    name_score = 'NAN'
  try:
    address_score = response['scores']['address_score']
  except:
    address_score = 'NAN'
  try:

    distance = response['scores']['distance']
  except:
    distance = 'NAAN'
  try:
    mapped_phone_count = response['scores']['mapped_phone_count']
  except:
    mapped_phone_count = 'NAN'
  error = response['error']
  final.append(id_data)
  final.append(merchant_ids)
  final.append(changed_mappings)
  final.append(status)
  final.append(name_score)
  final.append(address_score)
  final.append(distance)
  final.append(mapped_phone_count)
  final.append(error)
  final_data.append(final)

data = pd.DataFrame(final_data, columns=['ID','merchant_ids','changed_mappings','status','name_score','address_score','distance','mapped_phone_count','error'])
data.to_csv('/home/analytics/venv/Analytics/Discovery_Analytics/datta.csv', index=False)
