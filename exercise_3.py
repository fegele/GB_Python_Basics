# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(number_1, number_2, number_3):
    """The function takes three numbers and returns sum of two biggest numbers

    Parameters:
    number_1 (float)
    number_2 (float)
    number_3 (float)

    Returns:
    float: sum of two biggest arguments
    """
    func_result = number_1 + number_2 + number_3 - min(number_1, number_2, number_3)
    return func_result


input_1 = float(input("Enter number 1: "))
input_2 = float(input("Enter number 2: "))
input_3 = float(input("Enter number 3: "))
result = f'Sum of two biggest numbers = {my_func(input_1, input_2, input_3)}'
print(result)
