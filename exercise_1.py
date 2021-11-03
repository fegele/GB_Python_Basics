import sys


def salary(hours, salary_rate, bonus):
    result = hours * salary_rate + bonus
    return result


emp_hours = int(sys.argv[1])
emp_salary_rate = int(sys.argv[2])
emp_bonus = int(sys.argv[3])
month_salary = salary(emp_hours, emp_salary_rate, emp_bonus)
print(month_salary)
