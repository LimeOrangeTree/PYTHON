import pandas as pd

df1=pd.read_csv('data\\c1.csv')
df2=pd.read_csv('data\\c2.csv')
df3=pd.read_csv('data\\c3.csv')
print(df1)
print(df2)
print(df3)
# row1=pd.concat([df1,df2,df3])
# print(row1)
# print(row1.loc[3])
# print(row1.iloc[3])
# s1=pd.Series(['s1','s2','s3','s4'])
# print(pd.concat([df1,s1]))
# s2=pd.DataFrame([['s1','s2','s3','s4']],columns=['a','b','c','d'])
# print(s2)
# print('-'*30)
# print(pd.concat([df1,s2]))
# print(df1.append(s2))
# print(df1.append(s2,ignore_index=True))
# row1=pd.concat([df1,df2,df3],ignore_index=True)
# print(row1)
# s3=pd.DataFrame({'a':['s1'],'b':['s2'],'c':['s3'],'d':['s4']})
# print(s3)

col1=pd.concat([df1,df2,df3],axis=1)
print(col1)
print(col1['b'])
col2=pd.concat([df1,df2,df3],axis=1,ignore_index=True)
print(col2)
col1['new']=['n1','n2','n3','n4']
print(col1)

s5={'a':'s1','b':'s2','c':'s3','d':'s4'}
# print(df1.append(s5))
print(df1.append(s5,ignore_index=True))
print(df1.columns)
print(df2.columns)
print(df3.columns)
df2.columns=['e','f','g','h']
df3.columns=['a','b','f','h']
print(df1)
print(df2)
print(df3)
row1=pd.concat([df1,df2,df3])
print(row1)
print('-'*30)
print(pd.concat([df1,df3],join='inner'))
print(df1)
print(df2)
print(df3)
df2.index=[4,5,6,7]
df3.index=[0,2,6,7]
print(df1)
print(df2)
print(df3)
col1=pd.concat([df1,df2,df3],axis=1)
print(col1)
print(pd.concat([df2,df3],axis=1,join='inner'))
# merge:기본적으로 내부 조인







