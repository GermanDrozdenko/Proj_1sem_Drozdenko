# Вариант 6. В матрице элементы первого столбца возвести в куб.

import random

# генерация матрицы
matrix = [[0]*3 for i in range(3)]

# заполнение матрицы
for i in range(3):
    for j in range(3):
        matrix[i][j] = random.randint(-10, 10)

print("Исходная матрица:", matrix)

# изменение элементов первого столбца
for i in matrix:
    i[0] **= 3

print("Новая матрица:", matrix)