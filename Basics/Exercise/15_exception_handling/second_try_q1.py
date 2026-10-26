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

try:
    try:
        grade = float(input("Enter your grade (0-100): "))
    except ValueError:
        raise ValueError("Enter a number (0-100).")
    
    if grade < 0 or grade > 100: # don't use range(0, 101) here coz it will not include decimals like 85.5 since range() is only intended for whole numbers. 
        raise ValueError("Grade must be between 0 to 100.")
    # print(grade)

    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"
except ValueError as error:
    print(f"Problem: {error}")
else: # this runs if everything went well in try block
    print(letter)
finally:
    print("Thank you for using the Grade Calculator. Goodbye!")