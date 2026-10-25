# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]

# Write a program that asks you to enter an expense amount and program should 
# tell you in which month that expense occurred. If expense is not found then 
# it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]

amount = int(input("Enter an expense amount to find the month: "))

if amount == 2340:
    print("Jan")
elif amount == 2500:
    print("Feb")
elif amount == 2100:
    print("Mar")
elif amount == 3100:
    print("April")
elif amount == 2980:
    print("May")
else:
    print("No month match.")