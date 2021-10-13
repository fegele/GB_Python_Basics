# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("numbers.txt", 'w') as file:
    file.writelines(input("Enter numbers separated by spaces: "))

with open("numbers.txt", 'r') as file:
    numbers = file.readline().split()

number_list = [int(number) for number in numbers]
print(sum(number_list))
