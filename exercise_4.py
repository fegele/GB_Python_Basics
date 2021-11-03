users_input = input("Enter a sentence: ").split()
for key, word in enumerate(users_input):
    to_print = f'{key}: {word[:10]}'
    print(to_print)
