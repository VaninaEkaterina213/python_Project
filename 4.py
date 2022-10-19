import random
import heapq #c помощью этого мы можем находить наибольшие и наименьшие эл-ты массива
print("Введите длинну массива")
a=int(input())
array=[random.randint(1,200) for i in range(a)]
print("Сколько макс. чисел вы хотите вывести? (не превышайте указанную длинну массива, умоляю!!!)")
n=int(input())
from heapq import nsmallest # функция "nsmallest" из модуля "heapq" позволяет находить минимальные числа
res =nsmallest(n, array)# 1 аргумент - количество мин. чисел, 2 -то откуда брать числа
print(array)
print(res)