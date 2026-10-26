# Write a Python program that takes a numeric grade from the user (between 0 and 100), and prints the corresponding 
# letter grade:
# 90–100 → A  
# 80–89  → B  
# 70–79  → C  
# 60–69  → D  
# <60    → F

# Your program should handle the following exceptions:

# If the user enters a non-numeric value, catch the ValueError and display a user-friendly message.
# If the user enters a number outside the valid range (0 to 100), raise a ValueError yourself with a custom message.
# Use the try–except–else–finally structure:

# try: Attempt to parse the input and compute the letter grade.
# except: Handle conversion errors and invalid ranges.
# else: Print the final grade if everything was successful.
# finally: Print a goodbye message like "Thank you for using the Grade Calculator. Goodbye!" no matter what.

numeric_grade = int(input("Enter you marks (between 0 and 100): "))

try: 
    if numeric_grade in range(0, 101):
        if numeric_grade > 90 and numeric_grade <= 100:
            print("A is your grade.")
        elif numeric_grade in range(80, 90):
            print("B is your grade.")
        elif numeric_grade in range(70, 80):
            print("C is your grade.")
        elif numeric_grade in range(60, 70):
            print("D is your grade.")
        elif numeric_grade in range(0, 60):
            print("F is your grade.")
    if not numeric_grade in range(0, 101):
        raise ValueError("Marks outside the range. Try again.")
except Exception as e:
    print(f"Exception: {e}. Type: {type(e).__name__}")

print("Thank you for using the Grade Calculator. Goodbye!")
    

