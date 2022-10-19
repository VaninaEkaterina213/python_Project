import math
print ("выберите выражение a-f")
print("a) (101+0)/3 ","b) 3.0e-6 * 10000000.1","c) true && true","d) false && true","e) (false && false)|(true && true)","f) (false | false) && (true && true)" ,sep='\n')
a = input()
match a:
    case "a":
       print( (101 + 0) / 3)
    case "b":
       print(3.0e-6 * 10000000.1)
    case "c":
        print(True & True)
    case "d":
        print(False & True)
    case "e":
        print((False & False) | (True & True))
    case "f":
        print((False | False) & (True & True))
    case _:
        print("нет такой буквы!!!!!!!!!!!!!!!!")

