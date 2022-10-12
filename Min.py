#функции
def min(a,b,c):#минимум
    if(a<b and a<c ):
        print("Минимум: "+ str(a))
    elif (b<a and b<c):
        print("Минимум: "+ str(b))
    else:
        print("Минимум: " + str(c))
def num(x):#цифры числа
    s = 0#
    if x < 0:#
        x = x / -1
    while x != 0:#
        x = x // 10
        s = s + 1
    print(" в числе " + str(s) + " цифр")

def sumN(n):  #сумма цифр числа
    i = 0  #
    sum = 0  #
    while i != n:
        i = i + 1
        sum = sum + i
    print("сумма чисел " + str(sum))

def fuk (n):#факториал
    i = 0
    total = 1
    while i != n:
        i = i + 1
        total = total * i
    print("фактериал числа равен " + str(total))

#менюшка
print("Что вы хотите сделать?" + " 1- найти минимум 3-х чисел, 2- найти цифры числа,")
print(" 3 -найти сумму чисел от 1 до n, 4- найти факториал числа")
action=int(input())
match action:
    case 1:
        print("Введите 3 числа ")
        a = [int(input())
                for i in range(3)]
        min(a[0], a[1], a[2])
    case 2:
        print("введите число")
        x = int(input())
        num(x)
    case 3:
        print("введите количество чисел")
        n = int(input())
        sumN(n)
    case 4:
        print("введите натуральное число")
        n = int(input())
        if n <= 0:
            print("читать умеешь? Написано же НАТУРАЛЬНОЕ >:(")
        else:
            fuk(n)
    case _:
        print("Такого действия нет")

