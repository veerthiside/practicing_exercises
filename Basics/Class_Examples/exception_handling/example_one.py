x = input("Enter first number: ")
y = input("Enter second number: ")

# general exception
# try: 
#     z = int(x) / int(y)
# except Exception as e:
#     print(f"Exception: {e}")  
#     z = None  
    
# print(f"Division is {z}")

# specific exception
try: 
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("Division by zero error.")  
    z = None  
    
print(f"Division is {z}")