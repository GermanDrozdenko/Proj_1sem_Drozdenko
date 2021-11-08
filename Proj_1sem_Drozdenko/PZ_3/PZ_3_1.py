a = input("Введите целое число А: ")
b = input("Введите целое число B: ")
c = input("Введите целое число C: ")

while type(a) != int:                           #обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильный ввод")
        a = input("Введите целое число А: ")

while type(b) != int:                           #обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Неправильный ввод")
        b = input("Введите целое число B: ")

while type(c) != int:                           #обработка исключений
    try:
        c = int(c)
    except ValueError:
        print("Неправильный ввод")
        c = input("Введите целое число C: ")

if a<b<c:                                       #условие и вывод
    print("Высказывание истинно")
else:
    print("Высказывание ложно")