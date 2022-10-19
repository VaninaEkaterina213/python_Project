import random
print("Введите длинну массива")
a=int(input())
array=[random.randint(1,200) for i in range(a)]
n=0
m=0
sum = 0
for i in range(a):
    sum=sum +array[n]
    n=n+1
mid = sum/a
for j in range(a):
    if array[m]>mid:
        print(array[m])
    m = m+1
print(mid)
print(array)