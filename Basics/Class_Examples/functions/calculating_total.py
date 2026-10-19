def calculate_total(expense = 0): # here expense = 0 is a default variable. if you don't pass any argument to this function it will use 0 as an argument. 
    """
    This is a documentation string. It is used to tell the caller of the funtion what the funtion does.
    """
    total = 0
    for item in expense:
        total = total + item
    return total

tom_expense_list = [2100, 3400, 3500]
joe_expense_list = [200, 500, 700]
mark_expense_list = []

tom_total = calculate_total(tom_expense_list)
joe_total = calculate_total(joe_expense_list)
mark_total = calculate_total(mark_expense_list)

print("Tom's total is", tom_total)
print("Joe's total is", joe_total)
print("Mark's total is", mark_total)