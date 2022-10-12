def num(x):
    s = 0
    if x < 0:
        x = x / -1
    while x != 0:
        x = x // 10
        s = s + 1
    print(" в числе " + str(s) + " цифр")
print("введите число")
x = int(input())
num(x)
