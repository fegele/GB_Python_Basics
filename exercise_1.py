# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

import time


class TrafficLight:
    instance_id = 0

    def __init__(self, color):
        state_order = ['red', 'yellow', 'green']
        if self.instance_id > 0:
            previous_color = state.__color
            if state_order[state_order.index(color) - 1] == previous_color:
                self.__color = color
            else:
                print(f'Wrong color order: {color} after {previous_color}!')
                exit()
        else:
            self.__color = color

    def running(self):
        TrafficLight.instance_id += 1
        print(f'Traffic light shows {self.__color}')
        if self.__color == 'red':
            time.sleep(7)
        elif self.__color == 'yellow':
            time.sleep(2)
        elif self.__color == 'green':
            time.sleep(5)


# right order
my_list = ['red', 'yellow', 'green']
for color in my_list:
    state = TrafficLight(color)
    state.running()

# wrong order
my_list = ['red', 'green', 'yellow']
for color in my_list:
    state = TrafficLight(color)
    state.running()
