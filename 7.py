import random
print("Введите длинну массива")
a=int(input())
array=[random.randint(1,200) for i in range(a)]
n=0
chot= []
nechot= []
for i in range(a):
    if array[n]%2 ==0:
        chot.append(array[n])
    else:
        nechot.append(array[n])
    n = n +1
print(array,chot,nechot,sep='\n')
