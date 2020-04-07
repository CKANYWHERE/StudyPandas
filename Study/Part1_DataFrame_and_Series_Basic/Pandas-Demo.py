import pandas as pd
import numpy as np
import  seaborn as sns
import  folium

#people = {
#          "first": ["민","권","김","민"],
#          "last": ["창경","예진","지은","경휘"],
#          "email": ["chang@email.com","gown@email.com","eun@email.com","hui@email.com"]
#          }


df = pd.read_csv('../data/survey_results_public.csv') # Data 들고옴

#print(df['email']) #하나의 컬럼 가져올 떄
#print(df[['last','email','first']]) #여러개 컬럼 가져올 떄
#print(df.columns) #컬럼 값들 출력
#print(df.iloc[0]) #정수형으로 row값 가져올 떄
#print(df.iloc[[0,1]]) #row 겟수 정해서 가져올 때
#print(df.iloc[[0,1],0]) #row 갯수 정함 + 0번째 인덱스 가져옴
#print(df.loc[[0, 1],['email','last']]) #row 갯수 정함 + email,last 인덱스 가져옴
#print(df.shape) #row, column 카운트 출력
#print(df['Hobbyist'].value_counts()) #엑셀의 각각 값들의 카운트를 출력해줌
#print(df.loc[[0,1,2],'Hobbyist']) #1,2,3 row값들의 Hobbyist 컬럼을 출력
#print(df.loc[0:2,'Hobbyist']) #위와 동일
#print(df.loc[0:2,'Hobbyist':'Employment']) #위와 Hobbyist 컬럼부터 Employment 컬럼까지 출력

