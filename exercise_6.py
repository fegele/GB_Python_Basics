# Реализовать два небольших скрипта: итератор, генерирующий целые числа, начиная с указанного; итератор, повторяющий
# элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и cycle() модуля
# itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его
# завершения. Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

first_number = int(input("Enter the first number: "))
last_number = int(input("Enter the last number: "))
for number in count(first_number):
    if number > last_number:
        break
    else:
        print(number)

do_continue = 'Y'
letters = ['a', 'b', 'c', 'd']
for letter in cycle(letters):
    if do_continue == 'Y':
        print(letter)
    else:
        break
    do_continue = input("Print the next letter? Y/N >>> ")
