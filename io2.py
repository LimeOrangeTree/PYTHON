#프로그램실행시 특정폴더안의 내용을 모두 읽어 오기
# python io2.py data
# import sys
# import glob
# import os
# path=sys.argv[1]
# fileLists=glob.glob(os.path.join(path,"*.*"))
# for filename in fileLists:
#     print(filename)
#     with open(filename,'r',encoding='utf-8') as f:
#         print(f.read())
#         print('-'*50)

# import os
# f=open('data\\d1.txt','a')
# f=open(os.path.join('data','d1.txt'),'a')
# f.write('hello \n')
# f.write('python \n')
# f.write('welcome \n')
# f.close()

# d2.txt 파일 생성1~100
# with open(os.path.join('data','d2.txt'),'w') as f:
#     for i in range(1,101):
#         f.write(str(i)+"\n")


# python io2.py 생성할파일명
# python io2.py n1.txt
# import os
# titles=['이름','나이','주소']
# names=['이순신','강감찬','정약용','을지문덕']
# ages=['50','40','55','41']
# addr=['서울','부산','대전','서산']
# with open(os.path.join('data','d3.txt'),'w',encoding='utf-8') as f:
#     # print(titles)
#     # print(' | '.join(titles))
#     f.write(' | '.join(titles))
#     for i in range(len(names)):
#         row="\n{},{},{}".format(names[i],ages[i],addr[i])
#         f.write(row)
# # a=['1','2','3','4','5','6','7']
# # print(a)
# # print('-'.join(a))
# # print('&'.join(a))

#webtoon.csv -->webtoon.txt
import os
inputF=os.path.join('data','webtoon.csv')
outputF=os.path.join('data','webtoon.txt')
makeText=[]
with open(inputF,'r',encoding='utf-8') as f1:
    for line in f1:   #한줄씩 읽어서 line
        line=line.replace("https://","")
        makeText.append(line)
print(makeText)
with open(outputF,'w',encoding='utf-8') as f2:
    for line in makeText:
        f2.write(line)

# 실습)Beauty.smi파일을 읽어 자막문자열만 Beauty.txt파일로 저장






