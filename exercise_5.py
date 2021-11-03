class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} - запуск отрисовки.')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} - запуск отрисовки.')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} - запуск отрисовки.')


my_stationery = Stationery('Канцелярская принадлежность')
my_stationery.draw()

my_pen = Pen('Ручка')
my_pen.draw()

my_pencil = Pencil('Карандаш')
my_pencil.draw()

my_handle = Handle('Маркер')
my_handle.draw()
