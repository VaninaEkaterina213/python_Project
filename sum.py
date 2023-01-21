def sumN (n):#
    i = 0#
    sum = 0#
    while i != n:
        i = i + 1
        sum = sum + i
    print("сумма чисел " + str(sum))
print("введите количество чисел")
n = int(input())
sumN(n)