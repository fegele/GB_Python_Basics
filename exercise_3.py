# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

users_number = input("Enter a number n: ")
output = int(users_number) + int(users_number * 2) + int(users_number * 3)
print("n + nn + nnn =", output)

