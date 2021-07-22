# with open('data\\us-500.csv') as f:
#     for line in f:
#         print(type(line))
# ---------------------
# import csv
# with open('data\\us-500.csv') as f:
#     freader=csv.reader(f)
#     for line in freader:
#         print(line)
# --------------
import csv
# with open('data\\us-500.csv') as fr:
#     with open('data\\us-501.csv','w',newline='') as fw:
#         # fwriter=csv.writer(fw,quoting=csv.QUOTE_MINIMAL)
#         fwriter=csv.writer(fw,quoting=csv.QUOTE_MINIMAL,delimiter='*')
#         for line in csv.reader(fr):
#             fwriter.writerow(line)
#-------------------
# with open('data\\us-500.csv') as f:
#     for line in csv.DictReader(f):
#         print(line)
#-------------------
# with open('data\\movie3.csv',encoding='utf-8') as f:
#     for line in csv.DictReader(f,fieldnames=['title','score','rate','minute']):
#         print(line)
#-------------------
# data=[{'age':'23','height':'180','name':'홍길동','city':'서울'},
#       {'name':'임꺽정','height':'190','city':'서산','age':'30'},
#       {'name':'심청','height':'170','city':'광양','age':'20'}]
# with open("data\\student.csv","w",encoding="utf-8") as f:
#     fwriter=csv.DictWriter(f,['city','name','age','height'])
#     fwriter.writeheader()
#     fwriter.writerows(data)
#--data폴더내의 csv파일의 헤더를 제거하여 data1폴더에 저장-------
import os
import csv
def saveFile(filename):
    temp=[]
    cnt=0
    with open(os.path.join('.','data',filename),encoding='utf-8') as fr:
        for row in csv.reader(fr):
            if cnt==0:
                cnt = cnt + 1
                continue
            cnt = cnt + 1
            temp.append(row)
    with open(os.path.join('.','data1',filename),'w',encoding='utf-8',newline='') as fw:
        fwriter=csv.writer(fw)
        for row in temp:
            fwriter.writerow(row)
def main():
    os.makedirs(os.path.join('.','data1'),exist_ok=True)
    # print(os.listdir(os.path.join('.','data')))
    for filename in os.listdir(os.path.join('.','data')):
        if not filename.endswith('.csv'):
            continue
        # print(filename)
        saveFile(filename)
if __name__=='__main__':
    main()