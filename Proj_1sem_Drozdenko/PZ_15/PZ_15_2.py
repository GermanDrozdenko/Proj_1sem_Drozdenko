# Вариант 6. Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.

import random

# генерация матрицы
matrix = [[0]*3 for i in range(3)]

# заполнение матрицы
for i in range(3):
    for j in range(3):
        matrix[i][j] = random.randint(0, 50)

print("Исходная матрица:", matrix)

# замена элементов матрицы
for i in range(3):
    for j in range(3):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

print("Новая матрица:", matrix)