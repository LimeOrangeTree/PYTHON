import os
# # os.walk(경로)  for 문을 통해 하위디렉토리 순회
# # folder_name
# # subfolders
# # filenames
# print(os.walk('e:\\color'))
# for folder,subfolders,filenames in os.walk('e:\\color'):
#     print('현재폴더'+folder+'-------------------')
#     for subfolder in subfolders:
#         print('하위폴더'+subfolder)
#     for filename in filenames:
#         print('파일명'+filename)

# 압축하기
import zipfile
# one=zipfile.ZipFile('e:\\color.zip','w')  #집파일객체생성
# one.write('e:\\color\\basic1.py')
# one.close()

two=zipfile.ZipFile('e:\\two.zip','w')   #집파일객체생성
# print(os.getcwd())
os.chdir('e:\\color')    #현재위치 변경
# print(os.getcwd())
for folder,subfolders,filenames in os.walk('.'):
    two.write(folder)     #현재폴더생성
    # for subfolder in subfolders:   #서브폴더생성
    #     two.write(os.path.join(folder,subfolder))
    for filename in filenames:   #파일생성
        two.write(os.path.join(folder,filename))
two.close()






