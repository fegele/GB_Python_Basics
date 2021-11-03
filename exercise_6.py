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
