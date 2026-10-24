# ⭐⭐⭐
"""
3. Write a function called print_pattern that takes integer number as an argument
and prints following pattern if input number is 3,
*
**
***

if input is 4 then it should print

*
**
***
****

Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
"""

"""
output:
1. the pattern
input:
1. an integer that tell the length of the pattern
process:
1. take integer as an input (input)
2. print the pattern (output)
"""

""" for i in range(1, 5):
    print("*")

for i in range(1, 6):
    print("*", end="") """


def print_pattern(size): # say size = 3
    for line in range(size): # loop will execute for line = 0, line = 1, line = 2. running 3 times.
        for star in range(line+1): # loop will execute for line = 0, line = 1, line = 2. running 3 times. ???
            print("*", end="")
        print()

pattern_size = int(input("Enter the size of the pattern: "))
print_pattern(pattern_size)




"""
why stuck?
- unable to choose loop. - although i know that for would be the one, coz it makes no sense to repeat something
n number of times with if.
- # loop will execute for line = 0, line = 1, line = 2. running 3 times. ???    
"""    
"""
other note:
first loop:

"""