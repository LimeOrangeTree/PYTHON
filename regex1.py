# import pyperclip
# # print(pyperclip.paste())
# pyperclip.copy("Hello Python^^")
# 전화번호
# \d\d\d-\d\d\d\d-\d\d\d\d
# [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]
# [0-9]{3}-[0-9]{4}-[0-9]{4}
# 이메일주소
# [a-zA-Z0-9_]+@[a-zA-Z0-9]\.(com|co.kr|net)
# ^
# ^\d  :숫자로 시작
# [^0-9] :숫자가 아님
# import re
# p=re.compile(정규표현식)
# m=p.match(조사할문자열)
# print(re.match('a.b','aab'))
# print(re.match('a.b','a0b'))
# print(re.match('a.b','aab'))
# print(re.match('a.b','a b'))
# print(re.match('a.b','ab'))     None
# print(re.match('a[.]b','a.b'))
# print(re.match('a[.]b','a0b'))  None
# *,+
# print(re.match('ca*t','ct'))
# print(re.match('ca*t','caaaat'))
# print(re.match('ca*t','cat'))
# print(re.match('ca+t','ct'))    #None
# print(re.match('ca+t','caaaat'))
# print(re.match('ca+t','cat'))
# {m,n}   생략된 m =0,n=무한대(2억개미만)  {,5} {3} {3,}
# print(re.match('ca{2}t','ct'))     #None
# print(re.match('ca{2}t','cat'))  #None
# print(re.match('ca{2}t','caat'))
# print(re.match('ca{2,5}t','caat'))
# print(re.match('ca{2,5}t','caaaat'))
# print(re.match('ca{2,5}t','caaaaaaaaaaaaaat'))  #None
# ? 0 or 1
# print(re.match('ca?t','ct'))
# print(re.match('ca?t','cat'))
# print(re.match('ca?t','caaaat'))  #None
# --search,match
# p=re.compile('[a-z]+')
# m1=p.match('python')
# m2=p.match('33python')
# s1=p.search('python')
# s2=p.search('33python')
# print(m1)
# print(m2)
# print(s1)
# print(s2)
# f1=p.findall('33python')
# f2=p.findall('hello python ^^ ')
# print(f1)
# print(f2)
# phone=re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')
# r1=phone.match("my phone number is 010-1234-5678")
# r2=phone.search("my phone number is 010-1234-5678")
# r3=phone.findall("my phone number is 010-1234-5678")
# print(r1)
# print(r2)
# print(r3)
# print(r2.group())
# print(type(r2))
# -------
# p=re.compile('[a-z]+')
# r=p.search('33python99')
# print(r.group())
# print(r.start())
# print(r.end())
# print(r.span())
# 컴파일옵션
# DOTALL     (S)
# IGNORECASE (I)
# MULTILINE (M)
# VERBOSE   (X)
# r1=re.match('a.b','aab')
# r2=re.match('a.b','a\nb')
# print(r1)
# print(r2)
# r3=re.match('a.b','a\nb',re.S)
# print(r3)
# r4=re.match('[a-z]+','python',re.I)
# print(r4)
# r4=re.match('[a-z]+','Python',re.I)
# print(r4)
# r4=re.match('[a-z]+','PYTHON',re.I)
# print(r4)
# r4=re.match('[a-z]+','PYTHON')
# print(r4)
# p=re.compile('^python\s\w+')
# r1=p.match('python one two')
# print(r1)
# r1=p.match('java one two')
# print(r1)
# data="""python one
# two java three
# you need python^^
# python two three"""
# r2=p.match(data)
# print(r2)
# r3=p.findall(data)
# print(r3)
# p=re.compile('^python\s\w+',re.M)
# r2=p.match(data)
# print(r2)
# r3=p.findall(data)
# print(r3)
#그룹핑()
# r=re.search('(ABC)+','ABCABCABC BBB DDD')
# print(r)
# print('-'*30)
# phone=re.compile('(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
# r2=phone.search("my phone number is 010-1234-5678")
# print(r2)
# print(r2.group())
# print(r2.group(1))
# print(r2.group(2))
# print(r2.group(3))
# print(r2.group(0))   #모두출력
# print(r2.groups())   #튜플로 반환
# a,b,c=r2.groups()
# print(a,b,c)
# 문자열바꾸기
# sub(바꿀문자열,대상문자열)
# p=re.compile('(green|red|blue)')
# m=p.sub('color','red apples and green socks or blue eyes')
# print(m)
# m=p.sub('color','red apples and green socks or blue eyes',count=2)
# print(m)
# p=re.compile(r'\section')
# p=re.compile('\\section')
# p=re.compile(r'\\section')
# p=re.compile('\\\\section')
#-------------------
import pyperclip
import re
email=re.compile(r'''(
[a-zA-Z0-9_-]+         #username
@                       #@
[a-zA-Z0-9-]+           #domain name
(\.[a-zA-Z]{2,4}){1,2}  #.com  .co.kr
)''',re.VERBOSE)
def findText():
    text = pyperclip.paste()
    # print(text)
    result=email.findall(text)
    # print(len(result))
    # print(result)  # [(a,b),(),(),....]
    temp=[]
    for i in result:
        temp.append(i[0])
    # print(temp)
    return temp
def copyToClipboard(result):
    pyperclip.copy('\n'.join(result))
def main():
    result=findText()
    if len(result)>0:
        copyToClipboard(result)
        print('클립보드에 복사됨')
    else:
        print('일치하는 패턴없음')
if __name__=="__main__":
    main()

#--------------------------------
# fruit=['apple','mango','melon']
# f='-'.join(fruit)
# print(type(fruit),type(f))
# print(fruit)
# print(f)

