# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def user_data(name="unknown", surname="unknown", birth_year="unknown", city="unknown", email="unknown", phone="unknown"):
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
    user_data_list = ['name = ' + name,
                      'surname = ' + surname,
                      'birth_year = ' + birth_year,
                      'city = ' + city,
                      'email = ' + email,
                      'phone = ' + phone]
    result = ', '.join(user_data_list)
    return result


user_data_string = user_data(birth_year="1672", city="Saint P.", name="Peter", surname="Romanov")
print(user_data_string)
