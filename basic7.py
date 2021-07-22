a=['one','two','three']
b=['apple','banana','mango','orange','grape']
c=[1,2,3,4,5,6,7]

aa=zip(a,b)
print(list(aa))
aaa=zip(a,b,c)
print(list(aaa))
for i in range(len(a)):
# for i in range(len(c)): #i=0~6
    print(a[i],b[i],c[i])



