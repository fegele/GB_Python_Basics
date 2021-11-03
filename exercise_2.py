class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_amount(self):
        amount = 25
        depth = 5
        return self._length * self._width * amount * depth


road_1 = Road(20, 5000)
print(f'{road_1.calculate_amount()} kg')
