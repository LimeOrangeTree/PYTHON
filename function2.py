def add(a,b):
   c=a+b
   print('덧셈의 결과는 ',c)
def minus(a,b,c=1):
    d=a-b-c
    print('뺄셈의 결과는 ',d)
def mul(a=1,b=2,c=3):
    d=a*b*c
    print("곱셈의 결과는",d)
def plus(*i):
    print("넘어온 값",i)
    hap=0
    for j in range(len(i)):
        hap=hap+i[j]
    print("넘어온 값들의 합",hap)
def main():
    plus(10,20,30,40,50,60,70)
    plus(10,20)
    plus(10)
    plus()
    mul()
    mul(10)
    mul(10,20)
    mul(10,20,30)
    mul(c=99)
    mul(a=99,c=98)
    # add()
    add(10,20)
    add(300,400)
    # add(300,400,500)
    # minus(10,20,30,40)
    minus(10,20,30)
    minus(10,20)
    # minus(10)
    print(__name__)
if __name__=="__main__":
    main()




