import os
import pickle
#리스트나 딕션어리 형태를 그대로 유지하면서 파일로 저장
#확장자를 피클로 주면 알아보기 쉽다.dump 저장, load 불러오기.wb바이너리로 저장
fruit=['apple','banana','mango','watermelon']
# f=open(os.path.join('data','fruit.pickle'),'wb')
# pickle.dump(fruit,f)
# f.close()

# f=open(os.path.join('data','fruit.pickle'),'rb')
# a=pickle.load(f)
# f.close()
# print(a)

# people={'name':'park','age':20,'city':'seoul'}
# f=open('data\\people.pickle','wb')
# pickle.dump(people,f)
# f.close()

f=open('data\\people.pickle','rb')
p=pickle.load(f)
f.close()
print(p)
# shutil(shall util) : 파일, 디렉토리를 복사,이동,삭제,리네임을 수행
import shutil
# . 현재위치, .. 부모위치
# shutil.copy('.\\data\\Beauty.smi','.\\..\\b.txt')
# shutil.copy('data\\Beauty.smi','..\\c.txt')
# shutil.copy('data\\Beauty.smi','..\\..\\a.txt')  #상대경로
# shutil.copy('data\\Beauty.smi','e:\\d.txt')   #절대경로
# shutil.move('..\\..\\a.txt','..\\a.txt')    #상대경로
# shutil.move('e:\\d.txt','E:\\big\\d.txt')   #절대경로
# shutil.rmtree(경로)  디렉토리삭제





