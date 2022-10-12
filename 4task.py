def fuk (n):
    i = 0
    total = 1
    while i != n:
        i = i + 1
        total = total * i
    print("фактериал числа равен " + str(total))
print("введите натуральное число")
n = int(input())
if n <= 0:
    print("читать умеешь? Написано же НАТУРАЛЬНОЕ")
else:
    fuk(n)
