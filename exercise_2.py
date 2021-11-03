input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
output_list = [value for index, value in enumerate(input_list) if index > 0 and value > input_list[index-1]]
print(output_list)
