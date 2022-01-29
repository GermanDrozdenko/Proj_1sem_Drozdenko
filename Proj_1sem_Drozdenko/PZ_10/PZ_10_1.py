# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность
# из целых положительных и отрицательных чисел. Сформировать новый текстовый файл (.txt)
# следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Произведение элементов:
# Повторяющиеся элементы:
# Количество повторяющихся элементов:
# Элементы больше 5 увеличены в 2 раза:

first_file = open("firstFile.txt", "w", encoding="utf-8")
first_file.write("1 2 5 6 4 3 5 -1 2 -1 5 2")
first_file.close()
first_file = open("firstFile.txt", "r", encoding="utf-8")
indata = first_file.read()

amount = 0
for i in indata:
    if i.isdigit():
        amount += 1

multi = 1
for i in indata:
    if i.isdigit():
        multi *= int(i)

five = 2
for i in indata.split():
    if int(i) > 5:
        five *= int(i)

second_file = open("secondFile.txt", "w", encoding="utf-8")
second_file.write("Исходные данные: ")
second_file.write(indata)
second_file.writelines(['\nКоличество элементов: '])
second_file.write(str(amount))
second_file.writelines(['\nПроизведение элементов: '])
second_file.write(str(multi))
second_file.writelines(['\nПовторяющиеся элементы: '])
second_file.writelines(['\nКоличество повторяющихся элементов: '])
second_file.writelines(['\nЭлементы больше 5 увеличены в 2 раза: '])
second_file.write(str(five))
second_file.close()
second_file = open("secondFile.txt", "r", encoding="utf-8")
print(second_file.read())

first_file.close()
second_file.close()