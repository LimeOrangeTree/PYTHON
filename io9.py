def plus(a,b):
    return a+b

def writeToTextFile(a):
    f=open('e:\\big\\pythonStudy\\data\\io9.txt','a')
    f.write(str(a)+" is writed\n")

def main():
    writeToTextFile(plus(10,2))

if __name__=='__main__':
    main()
# 모듈설치(터미널에서)
# (venv) E:\big\pythonStudy>pip install pyinstaller
#                           pip uninstall pyinstaller
# 실행파일만들기
# pyinstaller --noconsole --onefile io9.py
#==> ‪E:\big\pythonStudy\dist\io9.exe
