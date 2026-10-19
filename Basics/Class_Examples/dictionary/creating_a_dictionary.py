my_dictionary = {"tom": 8899223311, "rob": 2233889944, "joe": 4433221188}
print(my_dictionary)

print(my_dictionary["tom"])

my_dictionary["sam"] = 8877665544
print(my_dictionary)

del my_dictionary["sam"]
print(my_dictionary)

# printing my_dictionary one by one
for key in my_dictionary:
    print("Key:", key, "Value:",my_dictionary[key])

# printing my_dictionary one by one using tuple
for k,v in my_dictionary.items():
    print("Key:", k, "Value:", v)

print("tom" in my_dictionary)

# deleting all key-value pair in my_dictionary
my_dictionary.clear()
print(my_dictionary)