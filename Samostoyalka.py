import random
def Task1():
    point_x= random.uniform(-1,1)
    point_y= random.uniform(-1,1)
    print("координаты точки:" + str(round(point_x,2))+ " "+ str( round(point_y,2)))
    if(((point_y<1) and (point_x>-1) and point_y>point_x+1) or ((point_y>-1) and (point_x>-1)and point_y<-point_x-1)or (point_y>-1 and point_x<1 and point_y<point_x-1)or (point_y<1 and point_x<1 and point_y>-point_x+1)):
        print("Точка входит в закрашенную область")
    else:
        print("Точка не входит в область")
def Task2():
    print("Введите день ")
    d=int(input())
    print("Введите время начала разговора")
    t=input()
    print ("Введите длительность разговора в минутах")
    dt= float(input())
    s=100.0
    print("стоимость минуты разговора "+str(s))
    s2 = s * dt
    if((t>=22.0 or t<=8.0)):
        if (d == 6 or d == 7):
            s2=(dt*s)-((dt*s)*0.3)
        if ((d<6)and (d>0)):
            s2=(dt*s)-((dt*s)*0.2)
    print(" День: " + str(d) + " Время: "+ str(t) + " Стоимость: " + str(s2))

def Task3():
    print("Выберите задание (a или б)")
    choose = input()
    match(choose):
        case "а":
            print("Введите A: ")
            a = int(input())
            print("Введите B: ")
            b = int(input())
            if (a % 2 == 0 and b % 2 != 0 or a % 2 != 0 and b % 2 == 0):
                print("Условие истинное")
            else:
                 print("Условие не истинное")
        case "б":
            print("Введите A: ")
            a = int(input())
            print("Введите B: ")
            b = int(input())
            print("Введите C: ")
            c = int(input())
            if(a%3==0 and b%3==0 and c%3==0):
                print("Условие истинно")
            else:
                print("Условие не истинное")
        case _:
            print("Такого задания нет")


print("Выберите задание от 1 до 3")
ch=input()
match(ch):
    case"1":
        Task1()
    case "2":
        Task2()
    case "3":
        Task3()
    case _:
        print("Такого задания нет :(")