# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (
# комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        result = ''
        if self.a != 0:
            result += f'{self.a}'
        if self.b < 0:
            if self.b != -1:
                result += f' - {abs(self.b)}i'
            else:
                result += f' - i'
        elif self.b > 0:
            if self.a != 0:
                result += f' + '
            if self.b != 1:
                result += f'{abs(self.b)}i'
            else:
                result += f'i'
        return result

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


number_1 = ComplexNumber(2, 3)
number_2 = ComplexNumber(-2, 1)
number_3 = number_1 + number_2
number_4 = number_1 * number_2
print(number_1, number_2, number_3, number_4, sep='\n')
