from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
client = MongoClient('mongodb+srv://pej2834:pej09180429@cluster0.ceosi8e.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url='http://know.nifos.go.kr/openapi/forestPoint/forestPointListSearch.do?localArea=42&gubun=emd&keyValue=5616322344776229063796515611583064046076&version=1.1&excludeForecast=1'

data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

emds=soup.find_all('emd')
emd=[]
for i in range(len(emds)):
    emd.append(emds[i].text)

gungus=soup.find_all('gungu')
gungu=[]
for i in range(len(gungus)):
    gungu.append(gungus[i].text)

maxis=soup.find_all('maxi')
maxi=[]
for i in range(len(maxis)):
    maxi.append(int(maxis[i].text))

#print(len(emd), len(gungu), len(maxi))
#print(emd[297])
total_list=[]
for i in range(len(maxi)):
    fores_list=[int(maxi[i]),'강원도',emd[i],gungu[i]]
    total_list.append(fores_list)

total_list=sorted(total_list,reverse=True)
print(total_list)

#for i in range(len(total_list)):
#    doc={'order': i+1,
#         'doname':'강원도',
#         'emd':total_list[i][2],
#         'gungu':total_list[i][3],
#         'maxi':total_list[i][0]}
#    db.forests.insert_one(doc)

