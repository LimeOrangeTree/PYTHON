# --------------------------------------------------
# pandas 활용하여 자료 수집
# tsv 자료 정리
# 2019.03.12
# pandas 패키지 설치
# 그래프 그리기 matplotlib, seaborn 모듈 설치
# 한글처리
# --------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글처리
from matplotlib import font_manager, rc
fontname = font_manager.FontProperties(fname="malgun.ttf").get_name()
rc('font', family=fontname)

df = pd.read_csv("data\\gap.tsv", sep='\t')     # 구분 기호를 ,에서 탭으로 바꿔줌
# print(df)
# print(df.head())    # 앞의 5개 보기
# print(df.tail())    # 뒤의 5개 보기
# print(df.head(10))  # 앞의 n개 보기
#
# print(type(df))     # <class 'pandas.core.frame.DataFrame'>
# print(df.shape)     # 행렬 갯수 보여주는 함수 튜플 형태로 보여줌(1704, 6)
# print(df.shape[0])  # 행의 갯수만 출력 1704
# print(df.columns)   # 컬럼이름만 출력 Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='object')
# print(df.dtypes)    # 각 컬럼의 데이터 타입 -- 판다스의 object는 string, int64는 int, float64는 float
# print(df.info())    # dtypes: float64(2), int64(2), object(2)   memory usage: 80.0+ KB
#
# # 열 단위로 특정한 자료만 추출하기
# s1 = df['country']  # 컬럼 이름을 지정하여 출력
# print(s1)
# print(type(s1))     # <class 'pandas.core.series.Series'>   열이 한개일 때는 시리즈
#
# s2 = df[['country', 'continent']]   # 열을 한개 이상 추출할 때 대괄호 하나 더 쓰기
# print(s2)
# print(type(s2))     # <class 'pandas.core.frame.DataFrame'> 열이 두개 이상일 때는 데이터 프레임
# print(s2.tail(3))
#
# # 행 단위로 특정한 자료만 추출하기 (loc: index 기준, iloc: 행번호기준)
# # index : pands에서 지정한 순서번호, 자료 수정삭제에 따라 번호가 변경됨
# # iloc : 자료에 따라 지정된 눈에보이지 않는 순서번호, 변경되지 않음
# print('-'*100)
#
# print(df.loc[100])
# print(df.loc[30])
# # print(df.loc[-1])     # 인덱스에서는 -1 값이 지정되지 않음
# print(df.loc[df.shape[0]-1])    # 마지막 값 추출
# print(df.tail(1))               # 마지막 값 추출, shape와 출력 형태는 다름
# print(df.loc[[9, 99, 999]])     # 괄호 두개 써야함
#
# print(type(df.loc[df.shape[0]-1]))    # <class 'pandas.core.series.Series'>
# print(type(df.tail(1)))               # <class 'pandas.core.frame.DataFrame'>
#
# print(df.iloc[1])
# print(df.iloc[99])
# print(df.iloc[-1])
# print(df.iloc[[9,99,999]])      # 괄호 두개 써야함
#
# # 행과 열이 겹치는 자료만 추출(슬라이싱)
# df1 = df.loc[:,['year','pop']]
# print(df1)
# # df1 = df.loc[:, [2,4]]    # 에러 KeyError: "None of [Int64Index([2, 4], dtype='int64')] are in the [columns]"
# df1 = df.iloc[:, [2,4,-1]]
# df1 = df.iloc[:, [0,1,2,3]]
# print(df1.head())
# print(list(range(4)))   # [0, 1, 2, 3]
# df1 = df.iloc[:, list(range(4))]
# print(df1.head())
#
# # range 함수를 이용하여 'country', 'year',  'pop' 추출하여 마지막 데이터만 출력
# # df2 = df.iloc[:, list(range(0, 6, 2))]
# df2 = df.loc[:,['country', 'year',  'pop']]
# print(df2.tail(1))
#
# # 100 행부터 200 행까지 데이터 추출
# df2 = df.loc[100:200, ['country', 'year',  'pop']]
# # df2 = df.iloc[101:201, list(range(0, 6, 2))]
# print(df2)
#
# # 연도별로 그룹화하여 lifeExp의 평균을 구하기
# print('-'*100)
#
# # 1번 방법
# year_group = df.groupby('year')
# year_group_life = year_group['lifeExp']
# print(year_group_life.mean())
#
# # 2번 방법
# print(df.groupby('year')['lifeExp'].mean())
#
# # 연도별, 대륙의 lifeExp의 평균을 구하기
# print(df.groupby(['year', 'continent'])['lifeExp'].mean())
# print(df.groupby('continent')['country'].nunique())
# ----------------------------------
# 그래프 그리기
# import matplotlib as plt
# import seaborn as sns
#
# data = sns.load_dataset('anscombe')
# # print(data['dataset'] == 'I')   # T/F로 출력됨
# # print(data['x']>10)             # T/F로 출력됨
#
# # 불린 추출
# print(data[data['x']>10])
#
# # dataset이 4 그룹인 것 추출
# print(data[data['dataset']=='IV'])
#
# print('-'*100)
# data1 = data[data['dataset']=='I']
# data2 = data[data['dataset']=='II']
# data3 = data[data['dataset']=='III']
# data4 = data[data['dataset']=='IV']
#
# print(data1)
# print(data2)
# print(data3)
# print(data4)
#
# print('-'*100)
#
# # 도화지 만들기
# fig = plt.figure()
#
# # 격자 만들기(영역 나누기)
# a1 = fig.add_subplot(2,2,1) # 첫번째 영역, 2행2열, 첫번재 칸
# a2 = fig.add_subplot(2,2,2)
# a3 = fig.add_subplot(2,2,3)
# a4 = fig.add_subplot(2,2,4)
#
# # 그래프 그리기
# a1.plot(data1['x'], data1['y'],'o')
# a2.plot(data2['x'], data2['y'],'ro')
# a3.plot(data3['x'], data3['y'],'go')
# a4.plot(data4['x'], data4['y'],'bo')
#
# # 그래프 제목 넣기
# a1.set_title('데이터1')        # 한글처리 안하면 한글 깨짐
# a2.set_title('데이터2')
# a3.set_title('데이터3')
# a4.set_title('데이터4')
# fig.tight_layout()
# # 그래프 보여주기
# plt.show()
# --------------------------------
# s1=df.groupby('year')['lifeExp'].mean()
# print(s1)
# print(type(s1))
# s1.plot()
# plt.show()
# ---mean(),max(),min()
# #1)lifeExp열을 추출하여 s1으로 할당
# s1=df['lifeExp']
# # print(s1)
# #2) s1의 가장큰값, 작은값, 평균 출력
# print(s1.max(),s1.min(),s1.mean())
# #3) s1에서 평균수명 보다 큰값만 출력
# print(s1>s1.mean())
# print(s1[s1>s1.mean()])
#
# a=[1,2,3,4]
# plt.plot(a,'o')
# plt.show()
# ------그래프----
tips=sns.load_dataset('tips')
print(tips)
print(type(tips))
print(tips['total_bill'].min())
print(tips['total_bill'].max())
fig=plt.figure()
a1=fig.add_subplot(111)
a1.plot(tips['total_bill'])
a1.set_title('음식비용')
a1.set_ylabel('식대')
plt.show()



