i = 1
psum = 0
msum = 0
for i in range(15):
    print("введите число")
    x = int(input())
    if x>=0:
        psum = psum + x
    else:
        msum = msum + x
print("сумма положительных" + " " + str(psum))
print("сумма отрицательных" + " " + str(msum))