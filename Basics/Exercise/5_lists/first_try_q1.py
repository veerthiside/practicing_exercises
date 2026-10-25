# Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#   3. March - 2600
#   4. April - 2130
#   5. May - 2190

# Create a list to store these monthly expenses and using that find out,

#     1. In Feb, how many dollars you spent extra compare to January?
#     2. Find out your total expense in first quarter (first three months) of the year.
#     3. Find out if you spent exactly 2000 dollars in any month
#     4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#     5. You returned an item that you bought in a month of April and
#     got a refund of 200$. Make a correction to your monthly expense list
#     based on this


# 1
expense_list = [2000, 2350, 2600, 2130, 2190]
months = ["Jan", "Feb", "March", "April", "May"]

feb_minus_jan = expense_list[1] - expense_list[0]
print(f"In Feb I spent ${feb_minus_jan} more than what I spent in Jan.")


# 2
first_three_months_expense = expense_list[0] + expense_list[1] + expense_list[2]
print(f"Total money spent in first three months is ${first_three_months_expense}.")


# 3
for i in range(len(expense_list)):
    if expense_list[i] == 2000:
        print(f"Yes in {months[i]} you spent $2000.") # LETS GOOOO. We solved this!!!


# 4
expense_list.append(1980)
print("List after adding May month's expense: ")
print(expense_list)            

# 5
expense_list[3] = expense_list[3] - 200
print("List after the refund in April: ")
print(expense_list) 