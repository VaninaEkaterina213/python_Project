print("введите 4 числа")
a = [int(input())
     for j in range(4)]
if a[0]==a[1]==a[2]==a[3]:
    print("равно")
else:
    print("не равно")