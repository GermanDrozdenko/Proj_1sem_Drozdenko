# Книжные магазины предлагают следующие коллекции книг:
# Магистр - Достоевский, Лермонтов, Пушкин, Тютчев.
# ДомКниги - Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет - Пушкин, Достоевский, Маяковский.
# Галерея - Чехов, Тютчев, Пушкин.
# Определить, в каких магазинах нельзя приобрести книги Грибоедова
# и Маяковского.

# создание множеств
magistr = {'Достоевский', 'Лермонтов', 'Пушкин', 'Тютчев'}
domKnigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bumMarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

# проверка наличия элемента во множествах
if 'Грибоедов' not in magistr:
    print("В магазине 'Магистр' нельзя приобрести книги Грибоедова.")
if 'Грибоедов' not in domKnigi:
    print("В магазине 'ДомКниги' нельзя приобрести книги Грибоедова.")
if 'Грибоедов' not in bumMarket:
    print("В магазине 'БумМаркет' нельзя приобрести книги Грибоедова.")
if 'Грибоедов' not in galereya:
    print("В магазине 'Галерея' нельзя приобрести книги Грибоедова.")

if 'Маяковский' not in magistr:
    print("В магазине 'Магистр' нельзя приобрести книги Маяковского.")
if 'Маяковский' not in domKnigi:
    print("В магазине 'ДомКниги' нельзя приобрести книги Маяковского.")
if 'Маяковский' not in bumMarket:
    print("В магазине 'БумМаркет' нельзя приобрести книги Маяковского.")
if 'Маяковский' not in galereya:
    print("В магазине 'Галерея' нельзя приобрести книги Маяковского.")
