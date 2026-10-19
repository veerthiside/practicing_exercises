expense = [2340, 2500, 2100, 3100, 2980]
total = 0

for i in range(len(expense)): 
    print("Month:", (i+1), "Expense:",expense[i])
    total = total + expense[i]

print("Total expense:", total)