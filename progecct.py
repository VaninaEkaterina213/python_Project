import random

alpha= dict( а = '00000', б = '00001', в = '00010', г = '00011', д = '00100', е = '00101', ж = '00110', з = '00111', и = '01000', й = '01001', к = '01010', л = '01011', м = '01100', н = '01101', о = '01110', п = '01111', р = '10000', с = '10001', т = '10010', у = '10011', ф = '10100', х = '10101', ц = '10110', ч = '10111', ш = '11000', щ = '11001', ь = '11010', ы = '11011', ъ = '11100', э = '11101', ю = '11110', я = '11111')
def alphavet(s):
    l2=list(s)
    l_s = len(l2)#длинна массива
    gg=[]
    ss = []

    for i in range (l_s):
        gg.append(alpha.get(l2[i],0))
        s2 = list(gg[i])
        for s in range (5):
            ss.append(int(s2[s]))
    pp=[]
    f = open('key.txt', 'w')
    rnd_1 = 0
    for j in range (l_s*5):
        rnd_1 = random.randint(0,1)
        pp.append(rnd_1)
        f.write(str(rnd_1))
    f.close()
    jopa=[]
    for jj in range(l_s*5):
        jopa.append(ss[jj]^pp[jj])
    str_jopa = ''.join(map(str,jopa))
    print(str_jopa)

def razshifr(s):
    #f2= open('key.txt', 'r')
    #print(f2.read())#
    with open("key.txt") as f2:
    stroka_from_key=(f2.read())
    p2=list(stroka_from_key)
    print(p2)
    s2=list(s)
    ss=[]
    pp=[]
    for s in range(5):
        ss.append(int(s2[s]))
        pp.append(int(p2[s]))
    print(ss)
    print(pp)
    #получить ключ 1-отксорить, 2-разделить и сравнить по алфавиту



print("Здравствуйте! Это программа для шифровки сообщения в двоичный код ( и разшифровки из него, разумеется)! ;>")
print("Выберите действие: Зашифровка - 'з'/ Расшифровка - 'р'")
action = input()
match action:
    case "з":
        print("Введите сообщеение без пробелов")
        mes=input()
        alphavet(mes.lower())


    case "р":
        print("Введите  зашифрованное сообщеение без пробелов")
        mes = input()
        razshifr(mes)

    case _:
        print("Такого действия нет")


