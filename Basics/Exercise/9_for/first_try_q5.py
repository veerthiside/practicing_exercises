# Write a program that prints following shape

# *
# **
# ***
# ****
# *****

n = 5
for line in range(1, 6):
    for star in range(line):
        print("*", end="")
    print()
    

