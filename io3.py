import os

def makeText(inputFile):
    results=[]
    with open(inputFile,'r',encoding='utf-8') as f1:
        for line in f1:
            line=line.replace('\n','')
            if len(line)<4:
                continue
            elif line.count(':') >3:
                continue
            results.append(line)
    return results
def makeFile(results):
    # print(results)
    with open(os.path.join('data','Beauty.txt'),'w',encoding='utf-8') as f2:
        for line in results:
            f2.write(line+'\n')

def main():
    inputF=os.path.join('data','Beauty.smi')
    results=makeText(inputF)
    makeFile(results)
if __name__=="__main__":
    main()
