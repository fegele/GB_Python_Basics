# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень. Подсказка: попробуйте решить задачу двумя
# способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def my_func(x, y):
    return x ** y


def my_func_loop(x, y):
    """Returns result of raising a number to a given power

    Parameters:
    x (float) - real positive number
    y (int) - negative natural number

    Returns:
    float: the first argument raised to the power of the second argument
    """
    func_result = 1
    if x == 0:
        print("invalid input")
    else:
        for i in range(abs(y)):
            func_result = func_result / x
        return func_result


number_1 = 2.36
number_2 = -3
print(my_func(number_1, number_2))
print(my_func_loop(number_1, number_2))
