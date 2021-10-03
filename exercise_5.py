# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные
# числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

my_list = [number for number in range(100, 1000 + 1) if number % 2 == 0]
print(reduce(lambda result, next_number: result * next_number, my_list))
