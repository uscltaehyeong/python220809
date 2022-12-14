#ifelse.py

#
value = 5
while value > 0 :
    print (value)
    value -=1

lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))


print("---break구문----")
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst :
    if item > 5:
        break
    print("Item:{0}".format(item))

print("---break구문----")
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst :
    if item%2==0:
        continue
    print("Item:{0}".format(item))

#수열함수
print(list(range(10)))
print(list(range(1,10)))
print(list(range(10,0,-1)))

#리스트내장
lst = list(range(1,11))
print([i**2 for i in list if i>5])

print("---필터링---")
lst = [10, 25, 30]
iterL=filter(None, lst)
for item in iterL:
    print(item)
/*
print("---필터링 함수 사용---")
def getBiggerThan20(i):
    return i > 20

lst = [10, 25, 30]
iterL = filter(getBiggerThan20,lst)
for item in iterL:
    print(item)
