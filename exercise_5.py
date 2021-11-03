result = 0
do_continue = True

while do_continue:
    numbers = input("Enter numbers with spaces or '=' to get the final sum: ").split()
    for item in numbers:
        if item != '=':
            result += int(item)
        else:
            do_continue = False
            break
    output = f'Sum of all entered numbers = {result}'
    print(output)
