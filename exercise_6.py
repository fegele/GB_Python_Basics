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
