# Даны два целых числа A и B (A < B).
# Найти сумму всех целых чисел от A до B включительно.

print("Введите два целых числа, при этом число A должно быть меньше числа B")
a = input("Введите целое число A: ")
b = input("Введите целое число B: ")

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильный ввод")
        a = input("Введите целое число A: ")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильный ввод")
        b = input("Введите целое число B: ")

s = 0

while a <= b:
    s += a
    a += 1

print("Сумма всех целых чисел: ", s)
