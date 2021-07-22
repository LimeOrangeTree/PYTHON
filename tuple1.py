#튜플 () 값 수정 안 된
a=(1,2,3,4,5)
print(type(a),a)
for i in range(len(a)):
    print(a[i])
print(a[:2])
# a[2]=10
print(a)
print(a*2)
b=("one","two")
print(a+b)
print(type(b))
b=list(b)
print(b)
b[0]='zero'
print(b)