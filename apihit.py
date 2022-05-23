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
from openpyxl.workbook import Workbook
import subprocess,smtplib,csv,os,requests,json,sys
from datetime import datetime,date,timedelta
import time

import smtplib,email,email.encoders,email.mime.text,email.mime.base
from httplib2 import Http

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
import pandas_gbq

import gspread_dataframe as gd
import pandasql as ps
from gspread_dataframe import get_as_dataframe, set_with_dataframe

datestring_d0 = datetime.strftime(datetime.now()-dt.timedelta(days=0),'%H-%M')
kal_ke_tareekh = datetime.strftime(datetime.now()-dt.timedelta(days=1),'%Y-%m-%d %H:%M')
aaj_ke_tareek = datetime.strftime(datetime.now()-dt.timedelta(days=0),'%Y-%m-%d')
current_hour = datetime.strftime(datetime.now()-dt.timedelta(days=0),'%H')

def runner_aryan(sql):
    with mdb.connect('mad.gc.magicpin.in','phpmyadmin','10ca1j0y','aryan',use_unicode=True, charset="utf8") as conn:
    # with mdb.connect('db.gc.magicpin.in','analytics','an@lytix10ca1','aryan') as conn:        
        conn.execute(sql)
        field_names = [[i[0] for i in conn.description]]
        data=conn.fetchall()
        data=map(list,data)
        data = data
        return data

def runner_walletdb(sql):
    with mdb.connect('paydbro.gc.magicpin.in','sherlock','solvem@gicpin','wallet',use_unicode=True, charset="utf8") as conn:
    #with mdb.connect('tpayro.gc.magicpin.in','sherlock','solvem@gicpin','wallet',use_unicode=True, charset="utf8") as conn:
        conn.execute(sql)
        field_names = [[i[0] for i in conn.description]]
        data=conn.fetchall()
        data=map(list,data)
        data =  data
        return data


def runner_helpdesk(sql):
    with mdb.connect('dbro.gc.magicpin.in','phpmyadmin','10ca1j0y','helpdesk',use_unicode=True, charset="utf8") as conn:
    # with mdb.connect('db.gc.magicpin.in','analytics','an@lytix10ca1','aryan') as conn:        
        conn.execute(sql)
        field_names = [[i[0] for i in conn.description]]
        data=conn.fetchall()
        data=map(list,data)
        data = data
        return data

def runner_walletdb(sql):
    with mdb.connect('paydbro.gc.magicpin.in','sherlock','solvem@gicpin','wallet',use_unicode=True, charset="utf8") as conn:
    # with mdb.connect('tpayro.gc.magicpin.in','sherlock','solvem@gicpin','wallet') as conn:
        conn.execute(sql)
        field_names = [[i[0] for i in conn.description]]
        data=conn.fetchall()
        data=map(list,data)
        data =  data
        return data

def runner_orderdb(sql):
    with mdb.connect('oms-analytics-db.gc.magicpin.in','analytics','an@lytics10ca1','delivery',use_unicode=True, charset="utf8") as conn:
    # with mdb.connect('tpayro.gc.magicpin.in','sherlock','solvem@gicpin','wallet') as conn:
        conn.execute(sql)
        field_names = [[i[0] for i in conn.description]]
        data=conn.fetchall()
        data=map(list,data)
        data =  data
        return data


reload(sys)
sys.setdefaultencoding('utf8')
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/analytics/venv/Analytics/Ghost/Christo/Chris_Task/Amruta/saurav_tiwari_sheets.json', scope)
gc = gspread.authorize(credentials)
sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1aTnQOWIvC3x4LSuHAgZgt_jM7GQZNyfEr4h3QbhoA9M/edit#gid=0')

#sheet_url = 'https://docs.google.com/spreadsheets/d/1lpOV5L-KSPCqJqZb7t72Pi-gmO2oofUVIC1OoC7wyq0/edit#gid=0'
def google_sheet_reader(sheet_name,col,sheet_url):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/analytics/venv/Analytics/Ghost/Christo/Chris_Task/Amruta/saurav_tiwari_sheets.json', scope)
    gc = gspread.authorize(credentials)
    sht2 = gc.open_by_url(sheet_url)
    sht = sht2.worksheet(sheet_name)
    if col ==0:
        c= get_as_dataframe(sht,evaluate_formulas=True)
        return c
    else:
        c= get_as_dataframe(sht,usecols=col,evaluate_formulas=True)
        return c
orderId=[949894,

12448760,
12593689]
resultDict = []
for i in orderId:
    try:       
        url = "http://10.140.1.123/merchant/ratings?uids="+str(i)+""
        payload={}
        #headers = {'apiKey': 'e7ILlc#$Zza1CND@0XRMdsprxf&EPJA!'}
        response = requests.request("GET", url, data=payload)
        response = json.loads(response.text)
        for x in response:
            print(x)
            avg_rank = x['rating']
            rating1 = x['rating_1']
            rating2 = x['rating_2']
            rating3 = x['rating_3']
            rating4 = x['rating_4']
            rating5 = x['rating_5']
            count_of_ratings = x['count']
            mid = x['merchant_id']

            #gift_card_no = x['redemptionPartnerCouponDto']['couponCodeToCustomer']
            final = []
            final.append(mid) 
            final.append(avg_rank)
            final.append(rating1)
            final.append(rating2)
            final.append(rating3)
            final.append(rating4)
            final.append(rating5)
            final.append(count_of_ratings)
            resultDict.append(final)
            #time.sleep(3)
    except:
        pass

data = pd.DataFrame(resultDict, columns=['mid','avg_rating','rating1','rating2','rating3','rating4','rating5','count_of_ratings'])

data.to_csv('/home/analytics/venv/Analytics/Ghost/Shivam/rating_big_table.csv', index=False)

print(data)


