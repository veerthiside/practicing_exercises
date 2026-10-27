# 1. Create a sample class named Employee with two attributes id and name
# employee :
#     id
#     name

# object initializes id and name dynamically for every Employee object created.

# emp = Employee(1, "coder")

# 2. Use del property to first delete id attribute and then the entire object

class Employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id

emp = Employee(1, "coder")
print(emp.id)
print(emp.name)

del emp.id
print(emp.name)
# print(emp.id)

del emp 
print(emp)