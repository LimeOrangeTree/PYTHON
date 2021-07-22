# python     io5.py      data        *.csv        total.csv
#          sys.argv[0] sys.argv[1]  sys.argv[2]   sys.argv[3]
# glob.glob(os.path.join(sys.argv[1],sys.argv[2]))
# data\*.csv 의 모든 내용을 total.csv로 저장
import sys
import os
import glob
path=sys.argv[1]
files=sys.argv[2]
result=sys.argv[3]
source=os.path.join(path,files)
print(source)
fileList=glob.glob(source)
temp=[]
for i in range(len(fileList)):    #0~2
    # print(fileList[i])
    f=open(fileList[i],'r',encoding='utf-8')
    for line in f:  #한줄씩 읽어서 line변수에 할당
        # print(line)
        temp.append(line)
    temp.append('----------------------------')
    temp.append('\n')
    f.close()
print(temp)
#
f2=open(os.path.join(path,result),'w',encoding='utf-8')
for i in range(len(temp)):
    f2.write(temp[i])
f2.close()



