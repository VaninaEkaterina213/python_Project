import random
print("Введите длинну массива")
a=int(input())
array=[random.randint(1,200) for i in range(a)]
n=0
max = []
m=0
for j in range(a-1):
    if array[n]>array[n+1] and array[n]>m:
        m = array [n]
    else:
        m = array[n+1]
    n = n+1
    max.append(array[n])
print(array)
print(max)