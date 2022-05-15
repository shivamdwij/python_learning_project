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
datestring_d0 = datetime.strftime(datetime.now() - timedelta(days = 8), '%Y-%m-%d')
kal_ke_tareekh = datetime.strftime(datetime.now()-dt.timedelta(days=1),'%Y_%m_%d')
aaj_ke_tareekh = datetime.strftime(datetime.now()-dt.timedelta(days=0),'%Y-%m-%d')
current_hour = datetime.strftime(datetime.now()-dt.timedelta(days=0),'%H')
kal = datetime.strftime(datetime.now()-dt.timedelta(days=1),'%Y-%m-%d')
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from elasticsearch import Elasticsearch

reload(sys)
sys.setdefaultencoding('utf8')
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/analytics/venv/Analytics/Ghost/Christo/Chris_Task/saurav_tiwari_sheets.json', scope)
gc = gspread.authorize(credentials)

#-------------------------- Enter Sheet URL onto which edit is to make------------------------------------------------

sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1YiviR3Pk2N8_UyPtDDQU72NcGBgs0QxgDV3fJITuXBY/edit#gid=169329236')

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
#-------------------- Enter URL which needs to be read----------------------------------------------------

sheet_id = 'https://docs.google.com/spreadsheets/d/1YiviR3Pk2N8_UyPtDDQU72NcGBgs0QxgDV3fJITuXBY/edit#gid=169329236'

def runner_walletdb(sql):
    try:
        db = mdb.connect('paydbro.gc.magicpin.in','sherlock','solvem@gicpin','wallet')
        cur1 = db.cursor()
        print('script is running.')
#----------------------------------------------------------------ENTER THE SQL QUERY HERE----------------------------------------------------------------------
        cur1.execute(sql)
        print (sql)
        field_names = [[i[0] for i in cur1.description]]
        field_names =field_names[0]
        arr=cur1.fetchall()
        arr= map(list, arr)
        arr = pd.DataFrame(arr, columns =field_names)
        # arr=field_names+arr
        return arr
    except Exception:
        print ('There is an exception')
        return None


def runner_aryan(sql):
    try:
        db =  mdb.connect('dbro.gc.magicpin.in','phpmyadmin','10ca1j0y','aryan',use_unicode=True, charset="utf8")
        cur1 = db.cursor()
        print ('script is running.')
#----------------------------------------------------------------ENTER THE SQL QUERY HERE----------------------------------------------------------------------
        cur1.execute(sql)
        print (sql)
        field_names = [[i[0] for i in cur1.description]]
        field_names =field_names[0]
        arr=cur1.fetchall()
        arr= map(list, arr)
        arr = pd.DataFrame(arr, columns =field_names)
        # arr=field_names+arr
        return arr
    except Exception:
        print ('There is an exception')
        return None


def runner_helpdesk(sql):
    try:
        db =  mdb.connect('db.gc.magicpin.in','phpmyadmin','10ca1j0y','helpdesk',use_unicode=True, charset="utf8")
        cur1 = db.cursor()
        print ('script is running.')
#----------------------------------------------------------------ENTER THE SQL QUERY HERE----------------------------------------------------------------------
        cur1.execute(sql)
        print (sql)
        field_names = [[i[0] for i in cur1.description]]
        field_names =field_names[0]
        arr=cur1.fetchall()
        arr= map(list, arr)
        arr = pd.DataFrame(arr, columns =field_names)
        # arr=field_names+arr
        return arr
    except Exception:
        print ('There is an exception')
        return None


def runner_orderdb(sql):
    try:
        db =  mdb.connect('34.93.208.27','delivery','delivery10ca1','delivery',use_unicode=True, charset="utf8")
        cur1 = db.cursor()
        print('script is running.')
#----------------------------------------------------------------ENTER THE SQL QUERY HERE----------------------------------------------------------------------
        cur1.execute(sql)
        print (sql)
        field_names = [[i[0] for i in cur1.description]]
        field_names =field_names[0]
        arr=cur1.fetchall()
        arr= map(list, arr)
        arr = pd.DataFrame(arr, columns =field_names)
        # arr=field_names+arr
        return arr
    except Exception:
        print ('There is an exception')
        return None

#--------------------------- Merchant Contact data --------------------------
sql_query_contact = """SELECT 
cat_id, count(case when count_of_store>0 then 1 else null end) as count_of_no from (
select m1.id, count(case when mcc.designation='Store_number' then 1 else null end) as count_of_store
         ,m1.category_id as cat_id
from merchant as m1 left join merchant_contact as mcc on m1.id=mcc.merchant_id
where m1.is_shadowed=0 and m1.is_closed=0 and highlight5 is null
group by 1 ) as sub_query
group by 1;"""


sql_query = runner_aryan(sql_query_contact)

#------------------------------ ENTER SHEET TAB NAME IN THE CURLY BRACES WE ARE USING (mx) AS THE SHEET NAME IS mx--------------------
sht4 = sht2.worksheet("DDLQ")
sht2.values_clear("DDLQ"!A1:B17")

gd.set_with_dataframe(sht4,sql_query)
print('Sheet Updated')

#-----------------------------------------Merchant Timings Data

sql_query_timings = """SELECT 
cat_id, count(case when count_of_store>0 then 1 else null end) as count_of_no from (
select m1.id, count(case when mcc.designation='Store_number' then 1 else null end) as count_of_store
         ,m1.category_id as cat_id
from merchant as m1 left join merchant_contact as mcc on m1.id=mcc.merchant_id
where m1.is_shadowed=0 and m1.is_closed=0 and highlight5 is null
group by 1 ) as sub_query
group by 1;"""

sql_query = runner_aryan(sql_query_timings)
sht4 = sht2.worksheet("DDLQ")
sht2.values_clear("DDLQ"+"!D1:E17")

gd.set_with_dataframe(sht4,sql_query)
print('Sheet Updated')
