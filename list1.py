# a=int(input("숫자1->"))
# b=int(input("숫자2->"))
# c=int(input("숫자3->"))
# d=int(input("숫자4->"))
# hap=a+b+c+d
# print(hap)
# 리스트
# 리스트명=[값1,값2,....]
# a=[1,2,3,4,5]  a[0],a[1],a[3]...
# aa=[0,0,0,0]
# aa[0]=int(input("숫자1->"))
# aa[1]=int(input("숫자2->"))
# aa[2]=int(input("숫자3->"))
# aa[3]=int(input("숫자4->"))
# hap=aa[0]+aa[1]+aa[2]+aa[3]
# print(hap)
# print(aa)
# print(len(aa))   #리스트aa의 길이
# ----
# animal=['cat','dog','bird']
# print(animal)
# print(animal[1])
# for i in range(3):  #0<=i<3  i=0,1,2
#     print(i,animal[i])
# print(len(animal))
# print('-'*30)
# for i in range(len(animal)):#0<=i<3  i=0,1,2
#     print(i,animal[i])
#
# for i in animal: # i=animal[0],animal[1],animal[2]
#     print(i)
# -----------
# mix=[1,2,3,"apple",[10,20]]
# print(mix)
# print(len(mix))
# print(mix[3])
# print(mix[4])
# for i in range(len(mix)): # i=0,1,2,3,4
#     print(mix[i])
# for i in mix: #i=mix[0],mix[1],mix[2],..mix[4]
#     print(i)
# print(mix[4])
# print(mix[4][0])
# print(mix[4][1])
# a=[10,20]
# a=['zero','one','two','three','four','five','six','seven']
# print(a)
# print(a[:])
# print(a[:3],a[1:-1],a[1:-1:2])  #[시작인덱스:끝인덱스:step(생략시1)]
# print(a[1::2])
# b=[1,2,3]
# print(b)
# #
# print(a+b)
# print(b*3)
# b[0]=100
# print(b)
# a[2]=b
# print(a)
# # 삭제
# del a[2]
# print(a)
# del a[:]
# print(a)
# 추가
# a=[89,12,5,8,3,1,2]
# print(type(a))
# print(type(a[2]))
# a.append(100)
# a.append(200)
# print(a)
# a.pop()        #마지막값 삭제
# print(a)
# a.remove(8)    #처음만나는 숫자8을 삭제
# print(a)
# a.sort()       #오름차순정렬
# print(a)
# a.reverse()    #내림차순 정렬
# print(a)
# aa리스트의 크기는 100이고 0,2,4,6,8 처럼 짝수로 초기화
# aa=[]
# for i in range(100):  #i=0,1,2,....99
#     aa.append(i*2)
# print(aa)
# bb리스트의 크기는 100이고 198,196,194,...0으로 초기화
# bb[0]=aa[99],bb[1]=aa[98],bb[2]=aa[97],.....
# bb=[]
# for i in range(100):
#    bb.append(aa[99-i])
# print(bb)

# aa.reverse()
# bb=aa
# print(bb)
#cc에 3의 배수 200개를 입력하고 10번째,20번째,....190,200번째 값을 출력하세요
# cc=[]
# for i in range(200):
#     cc.append((i+1)*3)
#     # if (i%9==0) & (i!=0):
#     #     print(cc[i])
# for i in range(9,200,10):
#     print(cc[i])

# my=[30,10,20]
# print("현재List %s"%my)
# my.append(40)
# print("append(40)후 %s"%my)
# my.pop()
# print("pop()후 %s"%my)
# my.sort()
# print("sort()후 %s"%my)
# my.reverse()
# print("reverse()후 %s"%my)
# print("20의 위치 %s"%my.index(20))
# my.insert(2,222)
# print("insert(2,222)후 %s"%my)
# my.remove(222)
# print("remove(222)후 %s"%my)
# my.extend([77,88,99])
# print("extend([77,88,99])후 %s"%my)
my=[30,10,20]
a=[89,12,5,8,3,1,2]
animal=['cat','dog','bird']
t=[]
t.append(my)
t.append(a)
t.append(animal)
                                # t=[]
                                # t.append(1)
                                # t.append(2)
                                # t.append(3)   t=[1,2,3]
# print(t)
# print(len(t))
for i in range(len(t)):  #i=0,1,2
    print("t[%s] 의 값 %s"%(i,t[i]))
    for j in range(len(t[i])):
        print(      "%s의 %s번째값 %s"%(t[i],j,t[i][j])       )




