# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте
# параметры, уникальные для каждого типа оргтехники.
#
# Продолжить работу над первым заданием. Разработайте методы,
# которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных
# о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру
# (например, словарь).
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип
# данных. Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках
# по ООП.

class Stock:
    item_id = 0

    def __init__(self):
        self.items = {'in stock': [],
                      'account department': [],
                      'human resources department': []}

    def is_in_list(self, department, item_id):
        for item in self.items[department]:
            if item_id == item['item_id']:
                return True
        return False

    def receive_device(self, item, unit=None):
        if unit:
            if self.is_in_list(unit, item.item_id):
                self.items[unit].remove(item.item_info)
                self.items['in stock'].append(item.item_info)
                print(f'{item.type} received from the {unit}')
            else:
                print(f'The item is not in the {unit}!')
        else:
            if not self.is_in_list('in stock', item.item_id):
                self.items['in stock'].append(item.item_info)
                print(f'{item.type} received')
            else:
                print('The item is already in stock!')

    def assign_device(self, item, unit):
        if self.is_in_list('in stock', item.item_id):
            self.items['in stock'].remove(item.item_info)
            self.items[unit].append(item.item_info)
            print(f'{item.type} assigned to the {unit}')
        else:
            print('The item is not in stock!')

    def __str__(self):
        stock_info = {}
        for department in self.items.keys():
            stock_info[department] = {}
            for item in self.items[department]:
                if item['type'] not in stock_info[department].keys():
                    stock_info[department][item['type']] = 1
                else:
                    stock_info[department][item['type']] += 1
        return str(stock_info)

    @staticmethod
    def input_item():
        item_data = {}
        attributes = {'printer': {'color': 'bw / color', 'speed': 'number, ppm', 'resolution': 'dpi'},
                      'scanner': {'format': 'A4 / A3', 'resolution': 'dpi'},
                      'copier': {'color': 'bw / color', 'speed': 'number, ppm'}}
        item_data['type'] = input("Input device type: ")
        print("Input device attributes.")
        item_attributes = {attribute: input(f'{attribute} ({value}): ') for attribute, value in
                           attributes[item_data['type']].items()}
        for key, value in item_attributes.items():
            item_data[key] = value
        return item_data


class InputTypeError(Exception):
    def __init__(self):
        self.txt = "Input error: wrong device type!"

    def __str__(self):
        return self.txt


class InputAttributeError(Exception):
    def __init__(self):
        self.txt = "Input error: wrong device attribute!"

    def __str__(self):
        return self.txt


class OfficeEquipment:
    def __init__(self, type):
        self.type = type
        Stock.item_id += 1


class Printer(OfficeEquipment):
    def __init__(self, item_data):
        type = item_data['type']
        if type != 'printer':
            raise InputTypeError
        else:
            color = item_data['color']
            speed = item_data['speed']
            resolution = item_data['resolution']
            if any((
                    color not in ['bw', 'color'],
                    not speed.isdecimal(),
                    not resolution.isdecimal()
            )):
                raise InputAttributeError
            else:
                super().__init__(type)
                self.item_id = Stock.item_id
                self.color = color
                self.speed = speed
                self.resolution = resolution

    @property
    def item_info(self):
        return {'item_id': self.item_id,
                'type': self.type,
                'color': self.color,
                'speed:': self.speed,
                'resolution': self.resolution}


class Scanner(OfficeEquipment):
    def __init__(self, item_data):
        type = item_data['type']
        if type != 'scanner':
            raise InputTypeError
        else:
            format = item_data['format']
            resolution = item_data['resolution']
            if any((
                    format not in ['A4', 'A3'],
                    not resolution.isdecimal()
            )):
                raise InputAttributeError
            else:
                super().__init__(type)
                self.item_id = Stock.item_id
                self.format = format
                self.resolution = resolution

    @property
    def item_info(self):
        return {'item_id': self.item_id,
                'type': self.type,
                'format': self.format,
                'resolutions:': self.resolution}


class Copier(OfficeEquipment):
    def __init__(self, item_data):
        type = item_data['type']
        if type != 'copier':
            raise InputTypeError
        else:
            color = item_data['color']
            speed = item_data['speed']
            if any((
                    color not in ['bw', 'color'],
                    not speed.isdecimal()
            )):
                raise InputAttributeError
            else:
                super().__init__(type)
                self.item_id = Stock.item_id
                self.color = color
                self.speed = speed

    @property
    def item_info(self):
        return {'item_id': self.item_id,
                'type': self.type,
                'color': self.color,
                'type:': self.type}


try:
    scanner_1 = Scanner(Stock.input_item())
except (InputTypeError, InputAttributeError) as error:
    print(error)

scanner_2 = Scanner({'type': 'scanner', 'format': 'A3', 'resolution': '300'})
printer_1 = Printer({'type': 'printer', 'color': 'bw', 'speed': '10', 'resolution': '600'})
printer_2 = Printer({'type': 'printer', 'color': 'color', 'speed': '30', 'resolution': '600'})
copier_1 = Copier({'type': 'copier', 'color': 'bw', 'speed': '15'})
copier_2 = Copier({'type': 'copier', 'color': 'bw', 'speed': '15'})

stock = Stock()
stock.receive_device(printer_1)
print(stock)
stock.receive_device(printer_2)
print(stock)
stock.receive_device(printer_2)
print(stock)
stock.receive_device(copier_1)
print(stock)
stock.receive_device(scanner_2)
print(stock)
stock.assign_device(printer_1, 'account department')
print(stock)
stock.assign_device(scanner_2, 'account department')
print(stock)
stock.assign_device(printer_2, 'human resources department')
print(stock)
stock.assign_device(printer_2, 'human resources department')
print(stock)
stock.receive_device(printer_2, 'human resources department')
print(stock)
stock.assign_device(printer_1, 'account department')
print(stock)
stock.receive_device(printer_1, 'account department')
print(stock)
print(stock.items)
