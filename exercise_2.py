# 1-2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_seconds = int(input("Enter time in seconds: "))

seconds = time_in_seconds % 60
minutes = time_in_seconds // 60 % 60
hours = time_in_seconds // 60 // 60

print(f"{time_in_seconds} seconds = "
      f"{hours} {'hour' if hours == 1 else 'hours'} "
      f"{minutes} {'minute' if minutes == 1 else 'minutes'} "
      f"{seconds} {'second' if seconds == 1 else 'seconds'} ")
