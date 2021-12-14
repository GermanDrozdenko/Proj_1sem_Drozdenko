# Даны три словаря на три элемента каждый. Объединить все словари в один.
# Вывести исходные словари и результирующий.

dict1 = {1:'fish', 2:'cat', 3:'dog'}
dict2 = {4:'table', 5:'chair', 6:'monitor'}
dict3 = {7:'paper', 8:'wood', 9:'metal'}

unionDict = {**dict1, **dict2, **dict3}

print("Исходные словари:", dict1, dict2, dict3)
print("Результирующий словарь:", unionDict)