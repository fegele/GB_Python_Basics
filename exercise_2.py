# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = []

while True:
    element = input("Type the next value or press Enter to end the input: ")
    if element:
        my_list.append(element)
    else:
        break

swapped_list = my_list.copy()

for element in swapped_list[1::2]:
    el_index = swapped_list.index(element)
    swapped_list.insert(el_index - 1, swapped_list[el_index])
    swapped_list.pop(el_index + 1)

print(my_list)
print(swapped_list)
