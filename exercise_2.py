# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class DevByZero(Exception):
    def __init__(self):
        self.txt = "Ошибка: деление на ноль!"

    def __str__(self):
        return self.txt


number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))
try:
    if number_2 == 0:
        raise DevByZero()
    print(number_1 / number_2)
except DevByZero as error:
    print(error)
