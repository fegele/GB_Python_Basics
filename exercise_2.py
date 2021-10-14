# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_fabric(self):
        pass

    @property
    def fabric(self):
        fabric = self.calc_fabric()
        return f'fabric needed: {fabric}'

    def __add__(self, other):
        result = self.calc_fabric() + other.calc_fabric()
        return f'Total fabric needed: {result}'

    def __str__(self):
        return f'{self.name}, {self.size}, {self.fabric}'


class Coat(Clothes):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V

    @property
    def size(self):
        size = self.V
        return f'{size=}'

    def calc_fabric(self):
        result = self.V / 6.5 + 0.5
        return round(result, 2)


class Suit(Clothes):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H

    @property
    def size(self):
        height = self.H
        return f'{height=}'

    def calc_fabric(self):
        result = 2 * self.H + 0.3
        return round(result, 2)


coat = Coat('Tweed coat', 45)
print(coat)

suit = Suit('Smart suit', 1.73)
print(suit)

print(coat + suit)
