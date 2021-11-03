def divide(dividend, divisor):
    """Returns division result

    Parameters:
    dividend (float)
    divisor (float)

    Returns:
    float: the first argument divided by the second argument
    """
    if divisor == 0:
        print("Error: Division by zero!")
    else:
        return dividend / divisor


number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))
result = divide(number_1, number_2)
if result:
    to_print = f'{number_1} / {number_2} = {result}'
    print(to_print)
