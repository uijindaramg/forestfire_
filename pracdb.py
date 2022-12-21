from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from urllib.request import urlopen
from selenium.webdriver.support.ui import Select
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pickle
import numpy as np
import datetime
import re

client = MongoClient('mongodb+srv://pej2834:pej09180429@cluster0.ceosi8e.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'http://know.nifos.go.kr/openapi/forestPoint/forestPointListSearch.do?localArea=42&gubun=emd&keyValue=5616322344776229063796515611583064046076&version=1.1&excludeForecast=1'

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

emds = soup.find_all('emd')
emd = []
for i in range(len(emds)):
    emd.append(emds[i].text)

gungus = soup.find_all('gungu')
gungu = []
for i in range(len(gungus)):
    gungu.append(gungus[i].text)

maxis = soup.find_all('maxi')
maxi = []
for i in range(len(maxis)):
    maxi.append(int(maxis[i].text))

total_list = []
for i in range(len(maxi)):
    fores_list = [int(maxi[i]), '강원도', emd[i], gungu[i]]
    total_list.append(fores_list)

total_list = sorted(total_list, reverse=True)
addressgungu = list(db.forestgunguandemd.find({}, {'_id': False}))

for j in range(len(total_list)):
    if addressgungu[0]['emd_post'] == total_list[j][2] and addressgungu[0]['gungu_post'] == total_list[j][3]:
        fores_list = [total_list[j][0], '강원도', addressgungu[0]['emd_post'], addressgungu[0]['gungu_post']]
        print(fores_list)



#
# print(addressgungu[0]['emd_post'])
# print(total_list)