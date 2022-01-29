# Из предложенного текстового файла (text18-6.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив все знаки пунктуации на знак "!"

file = open("text18-6.txt", "w", encoding="utf-8")
file.writelines(["Два дня мы были в перестрелке.\n"
                 "Что толку в этакой безделке?\n"
                 "Мы ждали третий день.\n"
                 "Повсюду стали слышны речи:\n"
                 "«Пора добраться до картечи!»\n"
                 "И вот на поле грозной сечи\n"
                 "Ночная пала тень.\n"])
file.close()

file = open("text18-6.txt", "r", encoding="utf-8")
data = file.read()
print(data)
amount = len(data.split(' ')) - 1
print("Количество пробельных символов:", amount)
print("")

newFile = open("newfile.txt", "w", encoding="utf-8")
newFile.write(data)
newFile.close()

newFile = open("newfile.txt", "r", encoding="utf-8")
print("Измененный текст:")
data = data.replace('?', '!')
data = data.replace('.', '!')
data = data.replace(':', '!')
print(data)

file.close()
newFile.close()

