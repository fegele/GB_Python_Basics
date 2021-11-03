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
