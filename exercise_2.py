# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def user_data(name="", surname="", birth_year="", city="", email="", phone=""):
    """Returns a string with available user data

    Parameters:
    name (string)
    surname (string)
    birth_year (string)
    city (string)
    email (string)
    phone (string)

    Returns:
    string: user data in format '<argument name> = <argument value>' concatenated with comma separator
    """
    result = f"name = {name if name != '' else 'unknown'}, " \
             f"surname = {surname if surname != '' else 'unknown'}, " \
             f"birth_year = {birth_year if birth_year != '' else 'unknown'}, " \
             f"city = {city if city != '' else 'unknown'}, " \
             f"email = {email if email != '' else 'unknown'}, " \
             f"phone = {phone if phone != '' else 'unknown'}"
    return result


user_name = input("Enter your name: ")
user_surname = input("Enter your surname: ")
user_birth_year = input("Enter your birth year: ")
user_city = input("Enter your city: ")
user_email = input("Enter your email: ")
user_phone = input("Enter your phone number: ")
user_data_string = user_data(birth_year=user_birth_year,
                             city=user_city,
                             name=user_name,
                             surname=user_surname,
                             email=user_email,
                             phone=user_phone)
# user_data_string = user_data(birth_year="1672", city="Saint P.", name="Peter", surname="Romanov")
print(user_data_string)
