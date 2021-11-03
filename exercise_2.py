class DevByZero(Exception):
    def __init__(self, divident):
        self.divident = divident
        self.txt = f"Error: division by zero in the operation ({divident} / 0)!"

    def __str__(self):
        return self.txt


number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))
try:
    if number_2 == 0:
        raise DevByZero(number_1)
    print(number_1 / number_2)
except DevByZero as error:
    print(error)
