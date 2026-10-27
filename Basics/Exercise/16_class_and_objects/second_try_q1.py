# 1. Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name

# object initializes id and name dynamically for every Employee object created.

# emp = Employee(1, "coder")

# 2. Use del property to first delete id attribute and then the entire object

class Employee: # making class Employee
    def __init__(self, id, name): # this runs automatically whenever we call Employee class. self means the object being built right now.
        self.id = id # this Employee's own id attribute gets the value that was passed in  
        self.name = name 

emp = Employee(1, "coder")
print(emp.id)
print(emp.name)

# note: id is also a name of python built-in function, use it here (since this project asks), but don't use it in future.

del emp.id
print(emp.name)
try: 
    print(emp.id)
except AttributeError as e:
    print(f"Error: {e}. Type of Error: {type(e).__name__}")

del emp 
try:
    print(emp)
except NameError as e:
    print(f"Error: {e}. Type of Error: {type(e).__name__}")