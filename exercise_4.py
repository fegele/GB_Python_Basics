# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

def translate_numbers(text):
    """Returns text with translated numbers (Zero to Nine)
    Parameters:
    text (string)
    Returns:
    string: text with numbers in words translated from English to Russian
    """
    eng_rus_dict = {
        'Zero': 'Ноль',
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
    }
    for key, value in eng_rus_dict.items():
        text = text.replace(key, value)
    return text


with open("file_eng.txt", 'r') as file_eng:
    text_eng = file_eng.readlines()
text_rus = []
for line in text_eng:
    text_rus.append(translate_numbers(line))
with open("file_rus.txt", 'w', encoding='utf-8') as file_rus:
    file_rus.writelines(text_rus)
