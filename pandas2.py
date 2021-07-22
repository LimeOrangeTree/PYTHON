import pandas as pd

# s1=pd.Series(['apple','watermelon',30])
# print(s1)
# print(type(s1))
# s1=pd.Series(['apple',1500])
# print(s1)
# s1=pd.Series(['apple',1500],index=['kind','price'])
# print(s1)
# s1=pd.Series(data=['apple',1500],index=['kind','price'])
# print(s1)
# 데이터프레임만들기
# d1=pd.DataFrame({
#     'name':['kim','lee','park'],
#     'city':['seoul','daejeon','jeju'],
#     'born':['1970-01-01','1980-02-02','1990-03-03'],
#     'died':['2015-12-30','2018-09-09','2017-06-07'],
#     'age':[50,40,30]
# })
# print(d1)
# print(type(d1))
# d1=pd.DataFrame({
#     'name':['kim','lee','park'],
#     'city':['seoul','daejeon','jeju'],
#     'born':['1970-01-01','1980-02-02','1990-03-03'],
#     'died':['2015-12-30','2018-09-09','2017-06-07'],
#     'age':[50,40,30]
# },index=['kim','lee','park'])
# print(d1)
d1=pd.DataFrame({
    'name':['kim','lee','park'],
    'city':['seoul','daejeon','jeju'],
    'born':['1970-01-01','1980-02-02','1990-03-03'],
    'died':['2015-12-30','2018-09-09','2017-06-07'],
    'age':[50,40,30]
},index=['kim','lee','park'],columns=['age','city','born','died']
)
print(d1)
# 순서가 보장된 딕션어리 생성
# from collections import OrderedDict
# d2=pd.DataFrame(OrderedDict([
#     ('name',['kim','lee','park']),
#     ('city',['seoul', 'daejeon', 'jeju']),
#     ('born', ['1970-01-01', '1980-02-02', '1990-03-03']),
#     ('died', ['2015-12-30', '2018-09-09', '2017-06-07']),
#     ('age', [50, 40, 30])
# ]))
# print(d2)
row=d1.loc['lee']
print(row)
print(type(row))
col=d1['age']
print(col)
print(type(col))
# 시리즈의 속성과 함수
# print(row.index)
# print(row.values)
# print(row.index[0])
# print(row.keys())
# print(row.keys()[1])
# print(col.index)
# print(col.values)
# print(col.min())
# print(col.max())
# print(col.mean())
# print(col.std())
# col에서 평균보다 큰데이터만 출력
# print(col>col.mean())
# print(col[col>col.mean()])
# print('='*30)
# print(col)
# print(col+col)
# print(col*col)
# print(col+1000)
# print(col*5)
# col2=pd.Series([3,5])
# print(col2)
# print(col+col2)
# col3=pd.Series([10,20,30,40,50])
# print(col3)
# print(col2+col3)
# print('+'*30)
# col4=col3.sort_index(ascending=False)
# print(col4)
# print(col3)
# print(col3+col4)
# print(d1)
# print(d1*3)
#
# print(d1['born'].dtype)
# print(d1['died'].dtype)
# borndate=pd.to_datetime(d1['born'],format='%Y-%m-%d')
# dieddate=pd.to_datetime(d1['died'],format='%Y-%m-%d')
# print(borndate)
# print(type(borndate))
# print(dieddate)
# print(d1)
# d1['borndate']=borndate    #열추가
# d1['dieddate']=dieddate
# print(d1)
# d1['lifeday']=d1['dieddate']-d1['borndate']
# print(d1)
# #열삭제drop()
# d3=d1.drop(['born'],axis=1)
# print(d3)
# d3=d3.drop(['died'],axis=1)
# print(d3)
# 저장
# city=d1['city']
# print(city)
# city.to_pickle('data\\city.pickle')
# d1.to_pickle('data\\d1.pickle')
city1=pd.read_pickle('data\\city.pickle')
print(city1)
d2=pd.read_pickle('data\\d1.pickle')
print(d2)
# # city1,d2를 city1.csv,d2.csv로 저장하세요
# d2.to_csv('data\\d2.csv')
# d2.to_csv('data\\d2.tsv',sep="\t")
# city1.to_csv('data\\city2.csv')
# col2=pd.Series([3,5])
# print(col2)
# col2.to_csv('data\\col2.csv')
# d2.to_excel('data\\d2.xlsx')
# d2.to_excel('data\\d3.xlsx',index=False)
#시리즈를 엑셀로
cityframe=city1.to_frame()
print(cityframe)
print(type(cityframe))
cityframe.to_excel('data\\cityframe.xlsx')

