print("Сколько чисел вы будите использовать?")
colvo=int(input())
print("введите 1 число")
num1 = int(input())
count=1
while count<colvo:
    print("введите следующее число")
    numx=int(input())
    print("выберите действие: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление, 5 - уравнение")
    action=input()
    if action == 1:
        if count ==1:
            sum = num1 + numx
        else:
            sum = sum + numx
    elif
