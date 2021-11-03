with open("new_file.txt", "a") as file:
    while True:
        input_line = input("Input some text of press Enter to exit: ").strip()
        if input_line != '':
            file.writelines(f'{input_line}\n')
        else:
            break
