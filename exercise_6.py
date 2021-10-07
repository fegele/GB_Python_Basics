# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий. Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика:   100(л)   50(пр)   20(лаб).
# Физика:   30(л)   —   10(лаб)
# Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

program_dict = {}
with open("learning_program.txt", 'r', encoding='utf-8') as file:
    program = file.readlines()

for line in program:
    subject = line.split(':')[0]
    splitted_line = line.split()[1:]
    lessons_number = 0
    for element in splitted_line:
        try:
            lessons_number += int(element.split('(')[0])
        except:
            continue
    program_dict[subject] = lessons_number

print(program_dict)
