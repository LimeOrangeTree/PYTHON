# f=open('data\\poem.txt','r',encoding="utf-8")
# # print(f.readline())
# while True:
#     line=f.readline()
#     if line=="":
#         break
#     print(line,end="")
# f.close()

# f=open('data\\poem.txt','r',encoding="utf-8")
# lines=f.readlines()
# # print(lines)
# for line in lines:
#     print(line,end="")
# f.close()

# f=open('data\\poem.txt','r',encoding="utf-8")
# line=f.read()
# print(line)
# f.close()

# with open('data\\poem.txt','r',encoding='utf-8') as f:
#     # print(f.read())
#     # print(f.readlines())
#     # print(f.readline())
#     for line in f:
#         print(line,end="")

# 파일경로 -리눅스와 맥 (/), 윈도우 (\)
# os모듈: os자원을 제어
# glob 모듈: 현재 디렉토리의 모든 파일을 리스트로 반환
import os
# print(os.getcwd())  #현재 작업디렉토리
# print(os.listdir())  #작업디렉토리 목록
# print(os.path.join('data','txt','0207','poem.txt'))
# os.chdir('E:\imgs')
# print(os.listdir())

import glob
# print(glob.glob('*'))
# print(glob.glob('*.py'))
#
# for filename in glob.glob('*'):
#     print(filename)

# filename=os.listdir('C:\Python\Python36')
filename=os.listdir(os.path.join('C:','Python','Python36'))
# print(filename)
# for fname in filename:
#     if fname.endswith('.exe'):
#         print(fname)

# p1="‪E:\\big\pythonStudy\\basic7.py"
# p2="‪E:\\big\pythonStudy\\data"
# print(os.path.dirname(p1))
# print(os.path.basename(p1))   #가장 마지막이름
# print(os.path.dirname(p2))
# print(os.path.basename(p2))
# python io1.py

# import sys
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# # python io1.py aaa bbb

import sys
path=sys.argv[1]
print(path)
# pathnames=path+'\\*.*'
pathnames=os.path.join(path,'*.*')
print(pathnames)
fileLists=glob.glob(pathnames)
print(fileLists)
# python io1.py C:\Windows
# python io1.py e:\big
