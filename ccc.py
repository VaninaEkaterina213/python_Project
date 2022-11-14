print ('Введите начало диапазона')
diapoz1 = int(input())
print ('Введите конец диапазона')
diapoz2 = int(input())
for i in range(diapoz1,diapoz2):
    delitel = 0#счётчик остаток 0
    for j in range(1, i + 1):
        if i % j == 0:
            delitel += 1
    if delitel <= 2:
        print(i)