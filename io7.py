#E:\big\pythonStudy 의 내용을 E:\big\backup 폴더를 생성한후 pythonStudy.zip파일로 생성
import zipfile
import os
def makeZip(folder):
    os.mkdir('E:\\big\\backup')   #집파일이 저장할 폴더생성
    os.chdir(folder)     #작업디렉토리이동
    # print(os.path.dirname(folder),os.path.basename(folder))
    filename=os.path.basename(folder)+".zip"
    path=os.path.join('E:\\big\\backup',filename)
    print(path)
    f=zipfile.ZipFile(path,'w')    #집파일객체생성
    for folder,subfolders,filenames in os.walk('.'):#압축하기
        f.write(folder)
        for filename in filenames:
            f.write(os.path.join(folder,filename))
    f.close() # 자원해제
def main():
    makeZip('E:\\big\\pythonStudy')
if __name__=="__main__":
    main()
# python io7.py c:\windows