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
