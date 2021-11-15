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
