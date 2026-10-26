x = input("Enter first number: ")
y = input("Enter second number: ")

# specific exception
try: 
    z = x / int(y) # int(x) to x
except ZeroDivisionError as e:
    print("Division by zero error.")  
    z = None  
except Exception as e:
    print(f"Exception type: {type(e).__name__}")
    z = None
    
print(f"Division is {z}")