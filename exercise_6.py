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
