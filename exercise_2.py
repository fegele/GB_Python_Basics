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
