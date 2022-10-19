#библиотеки
import math #матеша
import random #рандом
import heapq  # c помощью этого мы можем находить наибольшие и наименьшие эл-ты массива

#функции
def first_task():
    print ("выберите выражение a-f")
    print("a) (101+0)/3 ","b) 3.0e-6 * 10000000.1","c) true && true","d) false && true","e) (false && false)|(true && true)","f) (false | false) && (true && true)" ,sep='\n')
    a = input()
    match a:
        case "a":
            print( (101 + 0) / 3)
        case "b":
            print(3.0e-6 * 10000000.1)
        case "c":
            print(True & True)
        case "d":
            print(False & True)
        case "e":
            print((False & False) | (True & True))
        case "f":
            print((False | False) & (True & True))
        case _:
            print("нет такой буквы!!!!!!!!!!!!!!!!")

def second_task():
    print("введите 4 числа")
    a = [int(input())
         for j in range(4)]
    if a[0] == a[1] == a[2] == a[3]:
        print("равно")
    else:
        print("не равно")

def task_3():
    print("Введите длинну массива")
    a = int(input())
    array = [random.randint(1, 200) for i in range(a)]
    print("Сколько макс. чисел вы хотите вывести? (не превышайте указанную длинну массива, умоляю!!!)")
    n = int(input())
    from heapq import nlargest  # функция "nlargest" из модуля "heapq" позволяет находить максимальные числа
    res = nlargest(n, array)  # 1 аргумент - количество макс. чисел, 2 -то откуда брать числа
    print(array)
    print(res)

def task_4():
    print("Введите длинну массива")
    a = int(input())
    array = [random.randint(1, 200) for i in range(a)]
    print("Сколько макс. чисел вы хотите вывести? (не превышайте указанную длинну массива, умоляю!!!)")
    n = int(input())
    from heapq import nsmallest  # функция "nsmallest" из модуля "heapq" позволяет находить минимальные числа
    res = nsmallest(n, array)  # 1 аргумент - количество мин. чисел, 2 -то откуда брать числа
    print(array)
    print(res)

def task_5():
    print("Введите длинну массива")
    a = int(input())
    array = [random.randint(1, 200) for i in range(a)]
    n = 0
    m = 0
    sum = 0
    for i in range(a):
        sum = sum + array[n]
        n = n + 1
    mid = sum / a
    for j in range(a):
        if array[m] > mid:
            print(array[m])
        m = m + 1
    print(mid)
    print(array)

def task_6():
    print("введите 2 числа")
    a = int(input())
    b = int(input())
    c = 0
    for i in range(b):
        c = c + a
    print(c)

def task_7():
    print("Введите длинну массива")
    a = int(input())
    array = [random.randint(1, 200) for i in range(a)]
    n = 0
    chot = []
    nechot = []
    for i in range(a):
        if array[n] % 2 == 0:
            chot.append(array[n])
        else:
            nechot.append(array[n])
        n = n + 1
    print(array, chot, nechot, sep='\n')

def task_8():
    print("Введите градусы по Фаренгейту")
    f = int(input())
    print(str((f - 32) * (5 / 9)) + " C")

def task_9():
    print("введите свой рост и вес")
    height = int(input())
    weight = int(input())
    imt = weight / (height ** 2)
    print(imt)

def task_10():
    print("введите число")
    x = int(input())
    x2 = x ** 2
    x3 = x ** 3
    x4 = x ** 4
    print("квадрат числа " + str(x2), "куб числа " + str(x3), "4 степень числа " + str(x4), sep='\n')

def task_11():
    print("введите длины сторон треугольника")
    a = int(input())
    b = int(input())
    c = int(input())
    if c < a + b and b < a + c and a < b + c:
        print("треугольник с такими сторонами образовать можно")
    else:
        print("треугольник с такими сторонами образовать нельзя")

#меню

print("Выберите задание (1-11)")
act=int(input())
match act:
    case 1:
        first_task()
    case 2:
        second_task()
    case 3:
        task_3()
    case 4:
        task_4()
    case 5:
        task_5()
    case 6:
        task_6()
    case 7:
        task_7()
    case 8:
        task_8()
    case 9:
        task_9()
    case 10:
        task_10()
    case 11:
        task_11()
    case _:
        print("Такого задания нет")