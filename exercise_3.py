class WrongInput(Exception):
    def __init__(self, element):
        self.element = element
        self.txt = f"Error: '{element}' is not a number!"

    def __str__(self):
        return self.txt


result = []
while True:
    number = input("Enter a number or write 'stop' to end input: ")
    if number != 'stop':
        try:
            if not number.isdecimal():
                raise WrongInput(number)
            result.append(int(number))
        except WrongInput as error:
            print(error)
    else:
        break
print(result)
