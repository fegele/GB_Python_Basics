# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

users_input = input("Enter a sentence: ").split()
for key, word in enumerate(users_input):
    to_print = f'{key}: {word[:10]}'
    print(to_print)
