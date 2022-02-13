import subprocess
import MySQLdb as mdb
import sys
import json
from json import dumps
import csv
import requests
import smtplib
import datetime as dt
import pandas as pd
import numpy as np
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from decimal import *
from datetime import timedelta,date
from datetime import date
import subprocess,smtplib,csv,os,requests,json,sys
from datetime import datetime,date,timedelta
import time
import sys
import smtplib,email,email.encoders,email.mime.text,email.mime.base
from json import dumps
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from httplib2 import Http
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
import pandas_gbq
import gspread_dataframe
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread_dataframe as gd
import pandasql as ps
from gspread_dataframe import get_as_dataframe, set_with_dataframe

def google_sheet_reader(sheet_name,col,sheet_url):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/analytics/venv/Analytics/Ghost/Christo/Chris_Task/saurav_tiwari_sheets.json', scope)
    gc = gspread.authorize(credentials)
    sht2 = gc.open_by_url(sheet_url)
    sht = sht2.worksheet(sheet_name)
    if col ==0:
        c= get_as_dataframe(sht,evaluate_formulas=True)
        return c
    else:
        c= get_as_dataframe(sht,usecols=col,evaluate_formulas=True)
        return c

current_hour = datetime.strftime(datetime.now()-dt.timedelta(days=0),'%y_%m_%d_%H_%S')

datestring_d0 = datetime.strftime(datetime.now()-dt.timedelta(days=0),'%Y-%m-%d')

def runner_aryan(sql):
    with mdb.connect('dbro.gc.magicpin.in','phpmyadmin','10ca1j0y','aryan',use_unicode=True, charset="utf8") as conn:    
        conn.execute(sql)
        field_names = [[i[0] for i in conn.description]]
        data=conn.fetchall()
        data=map(list,data)
        data = data
        return data


final_data=google_sheet_reader("Dashboard",0,"https://docs.google.com/spreadsheets/d/1S-av6cKZxxKlXm36RqkjVeD1H62iVBBpsISxqRO9t6c/edit?hl=en&forcehl=1#gid=1577606444")
final_data=final_data.to_html(index=False, justify='center')
html= '<html> <body> <p> Hi All, </p> <p></p> <p> PFB Shutdown Cases Status: </p> </body> </html>' 
#html += '<html> <body> <p> <b>Shutdown Cases Report:- </b></p> <p></p>'
html += final_data

with open("/home/analytics/venv/Analytics/Ghost/Christo/Filed/content_sanity_checks123"+str(current_hour)+".html", "w") as file:
   file.write(html)
import imgkit

options={"xvfb": ""}
imgkit.from_file("/home/analytics/venv/Analytics/Ghost/Christo/Filed/content_sanity_checks123"+str(current_hour)+".html", "/home/analytics/venv/Analytics/Ghost/Christo/Filed/content_sanity_checks123"+str(current_hour)+".jpg",options=options)

from google.cloud import storage

def upload_to_google_cloud(bucket_name, source_file_name, destination_blob_name):

     storage_client = storage.Client.from_service_account_json('/home/analytics/venv/Analytics/Ghost/Christo/Chris_Task/gcp_image_upload_key.json', project='magicpin-14cba')
     bucket = storage_client.bucket(bucket_name) 
     blob = bucket.blob(destination_blob_name)
     blob.upload_from_filename(source_file_name)
     blob.make_public()
     image = blob.public_url
     print image
     image_data='https://img.magicpin.com/'+str(destination_blob_name)
     print image_data
     return image_data


selfie_image = "/home/analytics/venv/Analytics/Ghost/Christo/Filed/content_sanity_checks123"+str(current_hour)+".jpg"
uploaded_image = upload_to_google_cloud('magicpin-images',selfie_image,"Christo/Filed/content_sanity_checks123"+str(current_hour)+".jpg")


def main(url_sent1):
 url = 'https://chat.googleapis.com/v1/spaces/AAAAr9vWw_4/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=lxfP_u6dgHXSgK5IcO2uFPOLMBIANW5dRAlj9RaChVw%3D'
 bot_message = {"text":"*Shutdown Cases Report* "+str(datestring_d0)+"" ,"thread":{"name": "spaces/AAAAnovX6K4/threads/vsm6T-onpEQ"},

 "cards": [
   {
     "sections": [
       {
         "widgets": [
           {
             "image": {
               "imageUrl": url_sent1,
               "onClick": {
                 "openLink": {
                   "url": url_sent1
                 }
               }
             }
           }
         ]
       }
     ]
   }
 ]
}

 message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

 http_obj = Http()

 response = http_obj.request(
     uri=url,
     method='POST',
     headers=message_headers,
     body=dumps(bot_message),
 )

 print(response)

main(uploaded_image)

