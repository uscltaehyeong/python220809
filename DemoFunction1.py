#DemoFunction1.py
#함수 정의
def setValue(newValue):
    x = newValue

#호출
returnValue = setValue(5)
print(returnValue)

#함수 정의
def swap(x,y):
    return y,x

#호출
print(swap(3,4))

a=1.2
print(id(a))

def change(x):
    x[0]="H"

# 입력 데이터
wordlist=["J","A","M"]
change(wordlist)
print("호출후:", wordlist)

#리스트가 아닌경우
import copy
device ={"아이폰 : " 5, "아이패드 : " 10}
device2 = 