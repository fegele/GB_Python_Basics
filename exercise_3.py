# list
seasons = [['winter', 12, 1, 2], ['spring', 3, 4, 5], ['summer', 6, 7, 8], ['autumn', 9, 10, 11]]
month_number = int(input("Enter the number of the month from 1 to 12: "))

for season in seasons:
    if month_number in season:
        to_print = f"It's {season[0]} month."
        print(to_print)
        break

# dict
seasons = {
    'winter': [1, 2, 12],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
month_number = int(input("Enter the number of the month from 1 to 12: "))

for key, value in seasons.items():
    if month_number in value:
        to_print = f"It's {key} month."
        print(to_print)
        break
