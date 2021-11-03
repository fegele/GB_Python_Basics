class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} goes.')

    def stop(self):
        print(f'{self.name} stops.')

    def turn(self, direction):
        print(f'{self.name} turns {direction}.')

    def show_speed(self):
        print(f'speed: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'speed: {self.speed}')
        if self.speed > 60:
            print('Speed limit exceeded!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'speed: {self.speed}')
        if self.speed > 40:
            print('Speed limit exceeded!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


my_town_car = TownCar(80, 'blue', 'Mercedes')
print(f'\nNew car: name - {my_town_car.name}, color - {my_town_car.color}')
if my_town_car.is_police:
    print(f'{my_town_car.name} is a police car.')
else:
    print(f'{my_town_car.name} is not a police car.')
my_town_car.go()
my_town_car.show_speed()
my_town_car.turn('left')
my_town_car.stop()

my_sport_car = SportCar(150, 'red', 'Ferrari')
print(f'\nNew car: name - {my_sport_car.name}, color - {my_sport_car.color}')
my_sport_car.go()
my_sport_car.show_speed()
my_sport_car.turn('right')
my_sport_car.stop()

my_work_car = WorkCar(35, 'yellow', 'Opel')
print(f'\nNew car: name - {my_work_car.name}, color - {my_work_car.color}')
my_work_car.go()
my_work_car.show_speed()
my_work_car.turn('right')
my_work_car.stop()

my_police_car = PoliceCar(70, 'silver', 'BMW')
print(f'\nNew car: name - {my_police_car.name}, color - {my_police_car.color}')
if my_police_car.is_police:
    print(f'{my_police_car.name} is a police car.')
else:
    print(f'{my_police_car.name} is not a police car.')
my_police_car.go()
my_police_car.show_speed()
my_police_car.turn('around')
my_police_car.stop()
