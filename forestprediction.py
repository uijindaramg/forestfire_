# -*- coding: utf-8 -*-
import pandas as pd
import pickle
import warnings
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split


# 불필요한 경고 출력을 방지합니다.
warnings.filterwarnings('ignore')
forest = pd.read_csv('forest_realrealfinal원본파일.csv')

forest['특보내용']=forest['특보내용'].fillna("없음")
forest['시간단위풍속'] = forest['시간단위풍속'].fillna(forest['시간단위풍속'].mean())
forest['온도'] = forest['온도'].fillna(forest['온도'].mean())
forest['습도'] = forest['습도'].fillna(forest['습도'].mean())

forest['해안지역'] = 0
for i in range(674):

  if forest['발생장소_시군구'][i] == "고성":
    forest['해안지역'][i] = 1
  if forest['발생장소_시군구'][i] == "속초":
    forest['해안지역'][i] = 1
  if forest['발생장소_시군구'][i] == "양양":
    forest['해안지역'][i] = 1
  if forest['발생장소_시군구'][i] == "강릉":
    forest['해안지역'][i] = 1
  if forest['발생장소_시군구'][i] == "동해":
    forest['해안지역'][i] = 1
  if forest['발생장소_시군구'][i] == "삼척":
    forest['해안지역'][i] = 1

forest['피해면적크기']=1
for i in range(674):
  if (forest['피해면적_합계'][i]<1):
    forest['피해면적크기'][i]="small"
  if (forest['피해면적_합계'][i]>=5) & (forest['피해면적_합계'][i]<30) :
    forest['피해면적크기'][i]="mid"
  if (forest['피해면적_합계'][i]>=30):
    forest['피해면적크기'][i] = "big"
for i in range(674):
  if forest['발생장소_시군구'][i] == "강릉":
    forest['발생장소_시군구'][i] = "강릉시"
  if forest['발생장소_시군구'][i] == "고성":
    forest['발생장소_시군구'][i] = "고성군"
  if forest['발생장소_시군구'][i] == "동해":
    forest['발생장소_시군구'][i] = "동해시"
  if forest['발생장소_시군구'][i] == "삼척":
    forest['발생장소_시군구'][i] = "삼척시"
  if forest['발생장소_시군구'][i] == "속초":
    forest['발생장소_시군구'][i] = "속초시"
  if forest['발생장소_시군구'][i] == "양구":
    forest['발생장소_시군구'][i] = "양구군"
  if forest['발생장소_시군구'][i] == "양양":
    forest['발생장소_시군구'][i] = "양양군"
  if forest['발생장소_시군구'][i] == "영월":
    forest['발생장소_시군구'][i] = "영월군"
  if forest['발생장소_시군구'][i] == "원주":
    forest['발생장소_시군구'][i] = "원주시"
  if forest['발생장소_시군구'][i] == "인제":
    forest['발생장소_시군구'][i] = "인제군"
  if forest['발생장소_시군구'][i] == "정선":
    forest['발생장소_시군구'][i] = "정선군"
  if forest['발생장소_시군구'][i] == "철원":
    forest['발생장소_시군구'][i] = "철원군"
  if forest['발생장소_시군구'][i] == "춘천":
    forest['발생장소_시군구'][i] = "춘천시"
  if forest['발생장소_시군구'][i] == "태백":
    forest['발생장소_시군구'][i] = "태백시"
  if forest['발생장소_시군구'][i] == "평창":
    forest['발생장소_시군구'][i] = "평창군"
  if forest['발생장소_시군구'][i] == "홍천":
    forest['발생장소_시군구'][i] = "홍천군"
  if forest['발생장소_시군구'][i] == "화천":
    forest['발생장소_시군구'][i] = "화천군"
  if forest['발생장소_시군구'][i] == "횡성":
    forest['발생장소_시군구'][i] = "횡성군"
forest['습도'].replace(490,30,inplace=True)
forest['습도'].replace(366,30,inplace=True)
forest['산림면적'] = forest['산림면적'].str.split(',').str.join("")
forest['산림면적'] = forest['산림면적'].astype(int)
forest['피해면적(m^2)'] = 10000*forest['피해면적_합계']
forest['비율'] = forest['피해면적(m^2)']/forest['산림면적']
forest_small = forest[forest['피해면적크기']=="small"]
forest_small_ = forest_small.drop(['비율','피해면적_합계','시간단위풍속','해안지역','피해면적크기','산림면적'
                                    ,'재산피해금액','화재발생일자','화재진압시간','현장소방서거리','발생장소_시도',
                                   '발생장소_읍면','읍면동구분명','발화원인','발화열원명','발화요인소분류명','발화요인대분류명'
                                    ,'발화열원소분류명','최초착화물대분류명','전체인력수합계','시간단위풍향','발생일시_요일',
                                   '진화종료시간_년','진화종료시간_일','진화종료시간_시간','발생장소_관서','발생장소_동리',
                                   '발생원인_세부원인','발생원인_기타','물가상승배수'],axis=1)
forest_small_['진화종료시간_월']=forest_small_['진화종료시간_월'].astype(str)
forest_small_ = pd.get_dummies(forest_small_,columns=['발생장소_시군구','날씨','특보내용','발생원인_구분','계절','진화종료시간_월'])
forest_small_=forest_small_.drop(columns=['날씨_구름많음','날씨_구름조금', '날씨_맑음','날씨_비','날씨_소나기',
                                          '날씨_흐림','특보내용_강풍주의보','특보내용_건조경보','특보내용_건조주의보',
                                          '특보내용_없음','특보내용_풍랑경보','특보내용_풍랑주의보','특보내용_한파경보','특보내용_한파주의보'])

Y = forest_small_['피해면적(m^2)']
X = forest_small_.drop(['피해면적(m^2)'],axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
model = Ridge(alpha=10).fit(X_train, y_train)
pickle.dump(model, open('forest_prediction.pickle', 'wb'))
