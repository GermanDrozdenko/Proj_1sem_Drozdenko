# Дано вещественное число - цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

a = input("Введите стоимость 1 кг конфет: ")

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("Неправильный ввод")
        a = input("Введите стоимость 1 кг конфет: ")

n = 0.1
g = 0

while n <= 1:
    g += 100
    print("Стоимость за", g, "грамм: ", format(a * n, '.2f'))
    n += 0.1
