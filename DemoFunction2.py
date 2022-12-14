#DemoFunction2.py
#이름을 해석하는 규칙(local, Global, Built-in : LGB 규칙)
#전역변수
from unittest import result


x=5
#함수정의
def func1(a):
    return a+x
#호출
print(func1(1))

#함수정의
def func2(a):
    #지역변수
    x=2
    return a+x
#호출
print(func2(1))


#기본값이 있는 겨우
def times(a=10, b=20):
    return a*b

#호출
print( times())
print( times(5))
print( times(5,6))

#키워드 인자 방식(인자명을 기술)
def connectURI(server,port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURI("ycampus", "80"))
print(connectURI(port="80", server="ycampus"))

def union(*ar)
    #지역변수
    result=[]
    for item in ar:
        for x in item :
            if x not in result :
                result.append(x)
    return result

#호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))


