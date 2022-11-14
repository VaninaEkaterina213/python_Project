import random
array1 = [random.randint(1,200) for i in range (10)]
print(array1)
array2=[]
j=9
for i in range (10):
    array2.append(array1[j])
    j=j-1
print(array2)