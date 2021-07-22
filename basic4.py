# 조건문
# if 조건:
#     참인경우 수행문장1
#     참인경우 수행문장2
# a=int(input("숫자=>"))
# if a>300:
#     print("300보다 커요")
#     print("참인경우")
# print("if문 끝남")
# print("프로그램 종료")

# if 조건:
#     참인경우 수행문장들
# else:
#     거짓인 경우 수행문장들
# a=int(input("숫자=>"))
# if a>300:
#     print("300보다 커요")
#     print("참인경우")
# else:
#     print("300이하에요")
#     print("조건이 거짓인경우")
# print("if문 끝남")
# print("프로그램 종료")
# 숫자를 입력받아 짝수인지 홀수인지 출력
# a=int(input("숫자=>"))
# if a%2==1:
#     print("홀수")
# else:
#     print("짝수")
# 윤년여부 출력
# 년도를 입력받아 4로 나누어 떨어지고 100으로 나누어 떨어지지않으면 윤년
# 400으로 나누어 떨어져도 윤년
# year=int(input("년도-->"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("윤년")
# else:
#     print("윤년X")

# year=int(input("년도-->"))
# if (year%4==0 & year%100!=0) | (year%400==0):
#     print("윤년")
# else:
#     print("윤년X")

score=int(input("점수-->"))
if score>=90:
    print("A")
else:
    if score>=80:
        print("B")
    else:
        if score>=70:
            print("C")
        else:
            print("D")


