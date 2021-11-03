def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


n = int(input("Enter a number n: "))
for index, element in enumerate(fact(n)):
    print(f'{index + 1}! = {element}')
