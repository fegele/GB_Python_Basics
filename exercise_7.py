import json

with open("business_data.txt", 'r') as file:
    business_data = file.readlines()
data = {}
profits = []
for line in business_data:
    name = line.split()[0]
    profit = float(line.split()[2]) - float(line.split()[3])
    data[name] = profit
    if profit > 0:
        profits.append(profit)
avrg = sum(profits)/len(profits)
result = [data, {"average_profit": avrg}]
with open("analysis.json", "w") as write_f:
    json.dump(result, write_f)
