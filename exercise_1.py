# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date:
    date = None

    def __init__(self, date):
        self.date = date

    @classmethod
    def format_date(cls, date):
        cls.date = date
        result = [int(part) for part in cls.date.split('-')]
        return result

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    @staticmethod
    def validate_date(date):
        month_length = {
            1: 31,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        if 0 < date[1] <= 12:
            error = f'{date} - day number is wrong!'
            if date[1] == 2:
                if Date.is_leap_year(date[2]):
                    return date if date[0] <= 29 else print(error)
                else:
                    return date if date[0] <= 28 else print(error)
            else:
                return date if date[0] <= month_length[date[1]] else print(error)
        else:
            error = f'{date} - month number is wrong!'
            print(error)


date_1 = Date.format_date('12-03-2015')
date_1 = Date.validate_date(date_1)
if date_1:
    print(date_1)

date_2 = Date.format_date('12-13-2015')
date_2 = Date.validate_date(date_2)
if date_2:
    print(date_2)

date_3 = Date.format_date('31-09-2018')
date_3 = Date.validate_date(date_3)
if date_3:
    print(date_3)

date_4 = Date.format_date('29-02-2013')
date_4 = Date.validate_date(date_4)
if date_4:
    print(date_4)

date_5 = Date.format_date('29-02-2000')
date_5 = Date.validate_date(date_5)
if date_5:
    print(date_5)
