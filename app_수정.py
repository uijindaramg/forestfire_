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
model = pickle.load(open('forest_prediction.pickle', 'rb'))

app = Flask(__name__)


## URL 별로 함수명이 같거나,
## route('/') 등의 주소가 같으면 안됩니다.

@app.route('/')
def init():
    return render_template('forestfire_int.html')
@app.route('/predictget',methods=["POST"])
def push_2():
    cause_receive = request.form['cause_give']
    doc = {
        'cause_name': cause_receive,
    }
    db.forestcause.drop()
    db.forestcause.insert_one(doc)
    return jsonify({'msg': '주문 완료!'})

@app.route('/predict', methods=['GET'])
def machinelearning():
    click_forest = list(db.forestname.find({}, {'_id': False}))[0]['san_name']

    for i in range(124):
        if (list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['mt'].split(' ')[1] == click_forest):
            tem = list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['tmp']
            hum = list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['hm']
            result1 = float(tem)
            result2 = re.sub(r'[^0-9]', '', hum)
            list_addr = list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['addr']
            list_gungu = list_addr.split(" ")[1]
    if list_gungu == "강릉시":
        gungu01 = 1
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "고성군":
        gungu01 = 0
        gungu02 = 1
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "동해시":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 1
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "삼척시":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 1
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "속초시":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 1
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "양구군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 1
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "양양군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 1
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "영월군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 1
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "원주시":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 1
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "인제군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 1
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "정선군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 1
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "철원군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 1
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "춘천시":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 1
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "태백시":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 1
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "평창군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 1
        gungu16 = 0
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "홍천군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 1
        gungu17 = 0
        gungu18 = 0
    if list_gungu == "화천군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 0
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 1
        gungu18 = 0
    if list_gungu == "횡성군":
        gungu01 = 0
        gungu02 = 0
        gungu03 = 0
        gungu04 = 1
        gungu05 = 0
        gungu06 = 0
        gungu07 = 0
        gungu08 = 0
        gungu09 = 0
        gungu10 = 0
        gungu11 = 0
        gungu12 = 0
        gungu13 = 0
        gungu14 = 0
        gungu15 = 0
        gungu16 = 0
        gungu17 = 0
        gungu18 = 1
    current = datetime.datetime.today().month
    if (current == 3) or (current == 4) or (current == 5):
        season_spring = 1
        season_summer = 0
        season_autumn = 0
        season_winter =0
    if (current == 6) or (current == 7) or (current == 8):
        season_spring = 0
        season_summer = 1
        season_autumn = 0
        season_winter =0
    if (current == 9) or (current == 10) or (current == 11):
        season_spring = 0
        season_summer = 0
        season_autumn = 1
        season_winter =0
    if (current == 12) or (current == 1) or (current == 2):
        season_spring = 0
        season_summer = 0
        season_autumn = 0
        season_winter = 1
    if current == 1:
        month1 = 1
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 2:
        month1 = 0
        month2 = 1
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 3:
        month1 = 0
        month2 = 0
        month3 = 1
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 4:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 1
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 5:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 1
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 6:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 1
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 7:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 1
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 8:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 1
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 9:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 1
        month10 = 0
        month11 = 0
        month12 = 0
    if current == 10:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 1
        month11 = 0
        month12 = 0
    if current == 11:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 1
        month12 = 0
    if current == 12:
        month1 = 0
        month2 = 0
        month3 = 0
        month4 = 0
        month5 = 0
        month6 = 0
        month7 = 0
        month8 = 0
        month9 = 0
        month10 = 0
        month11 = 0
        month12 = 1
    cause = list(db.forestcause.find({}, {'_id': False}))
    if (cause[0]['cause_name'] == '건'):
        cause1 = 1
        cause2 = 0
        cause3 = 0
        cause4 = 0
        cause5 = 0
    if (cause[0]['cause_name'] == '기'):
        cause1 = 0
        cause2 = 1
        cause3 = 0
        cause4 = 0
        cause5 = 0
    if (cause[0]['cause_name'] == '담'):
        cause1 = 0
        cause2 = 0
        cause3 = 1
        cause4 = 0
        cause5 = 0
    if (cause[0]['cause_name'] == '쓰'):
        cause1 = 0
        cause2 = 0
        cause3 = 0
        cause4 = 1
        cause5 = 0
    if (cause[0]['cause_name'] == '입'):
        cause1 = 0
        cause2 = 0
        cause3 = 0
        cause4 = 0
        cause5 = 1
    arr = np.array([[result1, result2, gungu01, gungu02, gungu03, gungu04, gungu05, gungu06, gungu07, gungu08, gungu09,
                     gungu10,gungu11, gungu12, gungu13, gungu14, gungu15, gungu16, gungu17, gungu18,
                     cause1, cause2, cause3, cause4, cause5, season_autumn, season_winter, season_spring, season_summer,
                     month1, month10, month11, month12, month2, month3, month4, month5, month6, month7, month8,
                     month9]])
    arr_num = arr.astype(float)
    pred = model.predict(arr_num)
    output = pred[0]
    return jsonify({'output': output})

@app.route('/api',methods=["POST"])
def push():
    san_name_receive = request.form['san_name_give']
    doc = {
        'san_name': san_name_receive,
    }
    db.forestname.drop()
    db.forestname.insert_one(doc)
    return jsonify({'msg': '주문 완료!'})

@app.route('/forestfire_main.html')
def home():
    # # URL을 읽어서 HTML를 받아오고,
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # url = 'http://mtweather.nifos.go.kr/mount/local'
    #
    # #options = webdriver.ChromeOptions()
    # #options.add_argument("headless")
    #
    # res = requests.get(url)
    # soup = BeautifulSoup(res.text, 'html.parser')
    #
    # driver = webdriver.Chrome(ChromeDriverManager().install())#,options=options)
    #
    # # driver=webdriver.Chrome("C:\\Users\\samsung\\Desktop\\deep daiv\\chromedriver.exe")
    #
    # url = 'http://mtweather.nifos.go.kr/mount/local'
    # driver.get(url)
    #
    # list_tmp = []
    # list_rain = []
    # list_hm = []
    # list_ws = []
    # list_mt = []
    # list_addr = []
    #
    # url = 'http://mtweather.nifos.go.kr/mount/local'
    # driver.get(url)
    # driver.find_element(By.XPATH,'//*[@id="choiceTxt"]/ul/li[2]/a').click()
    #
    # for i in range(1, 125):
    #     for j in range(6):
    #         clicks = '//*[@id="choiceTxt"]/div/div/a[{}]'.format(i)
    #         driver.find_element(By.XPATH,clicks).click()
    #         html = driver.page_source
    #         soup = BeautifulSoup(html, 'lxml')
    #         list_addr.append(soup.find('span', {'data-ajax': 'addr'}).get_text())
    #         list_mt.append(soup.find('span', {'data-ajax': 'obsName'}).get_text())
    #         list_tmp.append(soup.find('span', {'data-ajax': 'tmpr'}).get_text())
    #         list_rain.append(soup.find('p', {'data-ajax': 'rain'}).get_text())
    #         list_hm.append(soup.find('p', {'data-ajax': 'hm'}).get_text())
    #         list_ws.append(soup.find('p', {'data-ajax': 'windspeed'}).get_text())
    #
    # df = pd.DataFrame(
    #     {'mt': list_mt, 'hm': list_hm, 'tmp': list_tmp, 'rain': list_rain, 'ws': list_ws, 'addr': list_addr})
    # df.drop_duplicates(['mt'], inplace=True)
    # df = df.iloc[1:, :]
    #
    # list_mt = list(df['mt'].values)
    # list_hm = list(df['hm'].values)
    # list_rain = list(df['rain'].values)
    # list_tmp = list(df['tmp'].values)
    # list_ws = list(df['ws'].values)
    # list_addr = list(df['addr'].values)
    #
    # for i in range(len(list_mt)):
    #     db.Ganwon_forestweather.update_one({'mt': list_mt[i]}, {
    #         '$set': {'tmp': list_tmp[i], 'addr': list_addr[i], 'hm': list_hm[i], 'rain': list_rain[i],
    #                  'ws': list_ws[i]}})

    click_forest = list(db.forestname.find({}, {'_id': False}))[0]['san_name']

    # driver.quit()

    for i in range(124):
        if (list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['mt'].split(' ')[1] == click_forest):
            list_ws=list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['ws']
            list_tmp = list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['tmp']
            list_rain = list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['rain']
            list_hm = list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['hm']
            list_addr = list(db.Ganwon_forestweather.find({}, {'_id': False}))[i]['addr']
            list_doname = list_addr.split(" ")[0]
            list_gungu = list_addr.split(" ")[1]
            list_emd = list_addr.split(" ")[2]

    return render_template('forestfire_main.html', temptext=list_tmp, temptext2=list_rain, temptext3=list_ws, temptext4=list_hm,
                           temptext5=click_forest, temptext6=list_doname, temptext7=list_gungu, temptext8=list_emd, temptext9=list_addr)

@app.route("/forestfire_main.html", methods=["GET"])

def forestnumber_get():
    all_users = list(db.forestname.find({}, {'_id': False}))
    return jsonify({'forestname': all_users[0]})


@app.route("/forest", methods=["GET"])
def forest_get():
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
    return jsonify({'forests': total_list})



@app.route('/forestfire_01.html')
def forest1():
    return render_template('forestfire_01.html')

@app.route('/forestfire_machinelearing.html')
def forestmachinelearing():
    return render_template('forestfire_machinelearing.html')

@app.route('/forestfire_02.html')
def forest2():
    return render_template('forestfire_02.html')

@app.route('/forestfire_03.html')
def forest3():
    return render_template('forestfire_03.html')

@app.route('/tableau.html')
def tableau():
    return render_template('tableau.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
