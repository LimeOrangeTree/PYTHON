# 리스트 [],튜플()
# a=[one,two,three]
# 딕션어리 {키:값,키:값,...}
# people={"name":"hong","age":21,1004:"yes"}
# print(type(people))
# print(people['name'])
# print(people[1004])
# # 키와 값추가
# people['hobby']='reading'
# print(people)
# # 삭제
# del people[1004]
# print(people)
#
# people['name']='park'
# print(people)
# people['body']=[180,70,30]
# print(people)
# # people[['apple','banana']]='fruit'    X
# print(people.keys())
# print(people.values())
# print(people.items())
# print('-'*30)
# for i in people.keys():   #i=name, age, hobby, body
#     print(people[i])
# print('='*30)
# for i in people.items():
#     print(i)
# print('#'*30)
# for k,v in people.items():
#     print(k,v)
# print(people)
# del people['name']
# print(people)
# people.clear()
# print(people)
# -집합(set)-------------------
a=set([1,3,5,7,9])
b=set([2,3,6,8,1,2])
print(a)
print(b)
print('합집합',a.union(b),a|b)
print('차집합',a.difference(b),b.difference(a),a-b,b-a )
print('교집합',a.intersection(b),a&b)

a.add(11)
print(a)
a.remove(5)
print(a)
a.update([21,23,25,27,29])
print(a)

