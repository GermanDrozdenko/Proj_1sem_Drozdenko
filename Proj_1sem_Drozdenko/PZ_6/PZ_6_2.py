# Дан список размера N. Найти максимальный из его локальных минимумов (локальный минимум - это
# минимум, который меньше любого из своих соседей.

n = int(input("Введите размер списка: "))

# создание пустого списка
list = []

# добавление элементов в список
for i in range(1, n+1):
    x = int(input("Введите число: "))
    list.append(x)

maxNumber = max(list)
print(list)

min = 0

# сравнение локальных минимумов и вывод максимального из них
for i in range(1, n - 1):
    if (list[i] < list[i-1] and list[i] < list[i+1]):
        min = list[i]
    if min > maxNumber:
        if list[i] > maxNumber:
            maxNumber == list[i]
print("Максимальный из локальных минимумов:", maxNumber)