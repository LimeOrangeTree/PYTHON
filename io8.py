import os,zipfile    #압축파일읽기
os.chdir('E:\\big\\backup')
# 집파일객체생성
one=zipfile.ZipFile('pythonStudy.zip')
print(one.namelist())
fileInfo=one.getinfo('basic1.py')
print(fileInfo.file_size)
print(fileInfo.compress_size)
one.close()