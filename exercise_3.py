class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            print('Invalid operation: the first cell is too small!')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number / other.number, 0))

    def make_order(self, number_in_line):
        result = f'{"*" * number_in_line}\n' * (self.number // number_in_line) + \
                 f'{"*" * (self.number % number_in_line)}\n'
        return result


cell_1 = Cell(4)
cell_2 = Cell(7)
cell_3 = cell_1 + cell_2
print(cell_3.number)
cell_4 = cell_1 - cell_2
cell_5 = cell_1 * cell_3
print(cell_5.number)
print(cell_5.make_order(10))
