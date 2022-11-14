import random
array1 = [random.randint(1,200) for i in range (10)]#nechot
array2 = [random.randint(1,200) for i in range (10)]#chot
array3 = []
for j in range (10):
    if array1[j]%2 != 0:
        array3.append(array1[j])
    if array2[j]%2 == 0:
        array3.append(array2[j])
print (array1,array2,array3,sep='\n')
