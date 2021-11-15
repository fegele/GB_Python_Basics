users_number = int(input("Enter a number: "))
max_digit = 0

while users_number > 0:
    digit = users_number % 10
    if digit > max_digit:
        max_digit = digit
    users_number = users_number // 10

print("The biggest digit in your number is", max_digit)
