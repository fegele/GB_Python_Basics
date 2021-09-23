# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

users_number = int(input("Enter a number: "))
max_digit = 0

while users_number > 0:
    digit = users_number % 10
    if digit > max_digit:
        max_digit = digit
    users_number = users_number // 10

print("The biggest digit in your number is", max_digit)
