with open('emp_data.txt', 'r', encoding='utf-8') as file:
    all_emp_data = file.readlines()
all_emp_salary = []
print("Employees with salary less than 20000:")
for line in all_emp_data:
    emp_data = line.split()
    all_emp_salary.append(float(emp_data[1]))
    if float(emp_data[1]) < 20000:
        print(emp_data[0])

avrg_salary = sum(all_emp_salary)/len(all_emp_salary)
print(f'\nAverage salary: {round(avrg_salary, 2)}')
