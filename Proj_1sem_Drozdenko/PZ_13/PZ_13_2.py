# Вариант 6. Составить генератор (yield), который переведет символы строки из верхнего регистра в нижний.

# перевод символов из верхнего регистра в нижний
def transform(text: str):
    for letter in text:
        yield letter.lower()

new_text = input("Введите текст: ")

# вывод объединенных в строку символов
print("Новый текст:", ''.join(transform(new_text)))
