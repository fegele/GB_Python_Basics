# 1-6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

start_distance = int(input("Enter the distance you ran on the first day (in kilometers): "))
target_distance = int(input("Enter your target distance: "))
days = 1

while start_distance < target_distance:
    start_distance = start_distance * 1.1
    days += 1
    # print(days, start_distance)

if days == 1:
    print("\nCongrats! You have already reached your goal!")
else:
    print(f"\nIf you increase your running distance by 10 percent every day, \n"
          f"you will reach your target distance on day {days}.")
