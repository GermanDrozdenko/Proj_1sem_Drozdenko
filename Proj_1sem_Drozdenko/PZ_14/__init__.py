# Вариант 6. Из исходного текстового файла (ip_address.txt) из раздела "Зарезервированные адреса"
# перенести в первый файл строки с ненулевыми первым и вторым октетами, а во второй - все остальные.
# Посчитать количество полученных строк в каждом файле.

import re

num1 = 0
num2 = 0

check = False

# Открытие и создание файлов
file = open('ip_address.txt', 'r')
result1 = open('result1.txt', 'w')
result2 = open('result2.txt', 'w')

# Создание шаблонов
pattern1 = re.compile(r'[0-9][0-9][0-9][.][0-9][0-9][0-9][.]')
pattern2 = re.compile(r'[0-9][0-9][0-9][.][0-9][0-9][.]')

for str in open('ip_address.txt'):
    # Переход к нужной строке
    flag = str.find('Зарезервированные адреса')
    if flag != -1:
        check = True
    if check:
        point = str.find('.')
        if point < 4 and point > 0:
            # Сортировка строк по шаблонам
            match1 = re.match(pattern1, str)
            match2 = re.match(pattern2, str)
            if match1 or match2:
                num1 += 1
                result1.write(str)
            else:
                num2 += 1
                result2.write(str)

# Вывод количества строк
print("Количество строк в первом файле:", num1)
print("Количество строк во втором файле:", num2)

# Закрытие файлов
file.close()
result1.close()
result2.close()