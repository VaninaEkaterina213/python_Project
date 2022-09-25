import math

print("вы хотите: 1 - решить квадратное уравнение, 2 - провести арфметические действия с числами")
act = int(input())
if act == 1:
    print("введите коофициэнты a, b, c")
    a = int(input())
    b = int(input())
    c = int(input())
    dis = b ** 2 - 4 * a * c
    if dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        print("x1=" + x1 + "x2=" + x2)
    elif dis == 0:
        x = -b / (2 * a)
        print("x=" + x)
    else:
        print("Корней нет")
elif act == 2:
    print("Сколько чисел вы будите использовать?")
    colvo=int(input())
    print("введите 1 число")
    total = int(input())
    count=1
    while count<colvo:
        print("введите следующее число")
        numx=int(input())
        print("выберите действие: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление")
        action=input()
        match action:
          case "1":
              total = total + numx
          case "2":
              total = total - numx
          case "3":
              total = total * numx
          case "4":
              total = total / numx
        count = count + 1
    print("результат" + str(total))
else:
    print("такого действия нет")