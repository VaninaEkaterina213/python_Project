def min(a,b,c):
    if(a<b and a<c ):
        print("Минимум: "+ str(a))
    elif (b<a and b<c):
        print("Минимум: "+ str(b))
    else:
        print("Минимум: " + str(c))
print("Введите 3 числа ")
a = [int(input())
     for i in range (3)]
min(a[0], a[1], a[2])


