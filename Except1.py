# a="hi! python"
# try:
#     print(a)
#     print(a[5])
#     # print(a[15])
#     print('출력이 다되었나요?')
# except:
#     print("프로그램을 확인하세요")
# print('프로그램종료')
# -------------------------
# def call(s,x,y):
#     try:
#         print(s)
#         print(s[10])
#         print(x/y)
#     except IndexError:
#         print('오류: 문자열의 길이가부족해요')
#     except ZeroDivisionError:
#         print('0으로 나누면 안되요')
#     except:
#        print("코드를 확인하세요")
#     else:
#         print("정상실행")
#     finally:
#         print("무조건실행")
#     print('함수끝---------------------')
#
# call('I like python',10,5)
# call('python',10,5)
# call('PythonOracle',10,0)
# call('PythonOracle','apple','banana')
# -------------------
# def call(s,x,y):
#     try:
#         print(s)
#         print(s[10])
#         print(x/y)
#     except IndexError as e:
#         print('오류: '+str(e))
#     except ZeroDivisionError  as e:
#         print('오류: ',e)
#     except:
#        print("기타오류")
#     else:
#         print("정상실행")
#     finally:
#         print("무조건실행")
#     print('함수끝---------------------')
#
# call('I like python',10,5)
# call('python',10,5)
# call('PythonOracle',10,0)
# call('PythonOracle','apple','banana')
# #----예외발생시키기
# def hap(a,b):
#     try:
#         s=a+b
#         if s<50:
#             raise ValueError("두수의 합은 50이 넘어야 되요")
#         print(s)
#     except ValueError as e:
#         print(e)
#     except:
#         print("기타")
#     finally:
#         print('함수끝----------------')
# hap(3, 4)
# hap(10, 60)
def sungjuk(name,kor,eng,mat):
    try:
        h=kor+eng+mat
        if len(name)<5:
            raise IndexError("이름은 5자리이상")
        elif h/3<80:
            raise ValueError("평균 80미만")
        print(name,h,h/3)
    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)
    except:
        print("코드확인")
    # 이름의 길이가 5자리가 안되면 IndexError발생
    # 평균이 80이 안되면 ValueError발생
    # print(이름,성적합,평균)
sungjuk('john',80,50,40)
sungjuk('alice',80,88,90)
sungjuk('Elizabeth',50,60,70)







# 예외처리 코드(함수, 호출?)






