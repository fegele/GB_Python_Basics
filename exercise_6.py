# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# structure = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})
# ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
# {
#     'название': ['компьютер', 'принтер', 'сканер'],
#     'цена': [20000, 6000, 2000],
#     'количество': [5, 2, 7],
#     'ед': ['шт.']
# }

# Create data structure from user's input

structure = []
item_index = 1
do_continue = 'y'

while do_continue == 'y':
    item = (item_index, {'name': input("Enter item name: "),
                         'price': input("Enter item price: "),
                         'number': input("Enter item number: "),
                         'unit': input("Enter item unit: ")})
    structure.append(item)
    do_continue = input("Type Y to continue or any other key to end the input: ").lower()
    item_index += 1

# Do analytics

analytics = {}

for item in structure:
    for key, value in item[1].items():
        if key not in analytics.keys():
            analytics[key] = [value]
        else:
            if value not in analytics[key]:
                analytics[key].append(value)

print(analytics)
