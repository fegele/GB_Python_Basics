time_in_seconds = int(input("Enter time in seconds: "))

seconds = time_in_seconds % 60
minutes = time_in_seconds // 60 % 60
hours = time_in_seconds // 60 // 60

print(f"{hours if hours > 9 else '0' + str(hours)}:"
      f"{minutes if minutes > 9 else '0' + str(minutes)}:"
      f"{seconds if seconds > 9 else '0' + str(seconds)}")
