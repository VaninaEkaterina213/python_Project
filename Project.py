#скелет проекта типо ок
print("Здравствуйте! Это программа для шифровки сообщения в двоичный код ( и разшифровки из него, разумеется)! ;>")
print("Для начала выберите язык: Ru- 'r'/Eng - 'e' ")
choose= input()
match choose:
    case "r":
        a="a" # это чтобы меня пайчарм за ошибки не избил
        # тут будет метод, выводящий русский алфавит
        # тут будет метод, выводящий русский двоичный алфавит
    case "e":
        a = "a"  # это чтобы меня пайчарм за ошибки не избил
        # тут будет метод, выводящий английский алфавит
        # тут будет метод, выводящий английский двоичный алфавит
print("Теперь выберите действие: Зашифровка - 'z'/ Разшифровка - 'r'")
action= input()
match action:
    case "z":
        a = "a"  # это чтобы меня пайчарм за ошибки не избил
        #тут будет метод зашифровки сообщения
    case "z":
        a = "a"  # это чтобы меня пайчарм за ошибки не избил
        # тут будет метод разшифровки сообщения