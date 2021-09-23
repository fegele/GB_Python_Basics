# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input("Enter your company's revenue: "))
expenses = int(input("Enter your company's expenses: "))

if revenue > expenses:
    print("Your business is profitable.")
    profit = revenue - expenses
    print(f"Profitability of your business: {round(profit / revenue * 100, 2)} %")
    employees_number = int(input("Enter the number of employees: "))
    print(f"Profit per employee: {round(profit / employees_number, 2)}")
else:
    print("Your business is not profitable.")
