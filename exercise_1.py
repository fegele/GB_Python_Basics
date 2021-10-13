# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        to_print = '\n'.join(
                       [''.join(
                           [f'{str(number):>5}' for number in list]
                       ) for list in self.list_of_lists])
        return to_print

    def __add__(self, other):
        result = [[num_1 + num_2 for num_1, num_2 in zip(list_1, list_2)]
                  for list_1, list_2 in zip(self.list_of_lists, other.list_of_lists)]
        return Matrix(result)


matrix_1 = Matrix([[8, -3, 12], [-5, 17, 2], [-3, 12, -7]])
print(f'The 1st matrix:\n{matrix_1}')

matrix_2 = Matrix([[-5, 13, 1], [14, 3, -7], [-6, 10, 15]])
print(f'The 2nd matrix:\n{matrix_2}')

sum_of_matrix = matrix_1 + matrix_2
print(f'Sum of matrix:\n{sum_of_matrix}')
