i = 1
sumo = 0
sump = 0
for i in range(15):
    print("введите число")
    a = int(input())
    if a>=0:
        sump += a
    else:
        sumo += a
print('Сумма отрицательных:', sumo, 'Сумма положительных:', sump, sep='\n')