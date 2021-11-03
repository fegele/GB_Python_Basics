my_list = [7, 5, 3, 3, 2]
users_input = int(input("Enter a number: "))

for item in my_list:
    if users_input > item:
        my_list.insert(my_list.index(item), users_input)
        break
    else:
        if my_list.index(item) == len(my_list) - 1:
            my_list.append(users_input)
            break

print(my_list)
