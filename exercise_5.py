from functools import reduce

my_list = [number for number in range(100, 1000 + 1) if number % 2 == 0]
print(reduce(lambda result, next_number: result * next_number, my_list))
