# ⭐⭐⭐
# SEE THE FORTH TRY. YOU UNDERSTOOD THIS QUESTION THERE.

# The pattern is made of lines, and each line is made of stars.

# for i in range(1, 5):
#     print("*")
# printing "*" 4 times

# so if user enters 3. i have to print line 3 times and on each line i have to print * in increasing order

def print_pattern(size):
    for line in range(size): # if size = 3. this loop will run 3 times.
        for star in range(line+1): # say line = 2, then this loop will run 2 times. so we added 1.
            print("*", end="")
        print()

pattern_size = int(input("Enter the size of the pattern: "))
print_pattern(pattern_size)

# why stuck?
# - why range(line+1)? - "for x in range(y): - this loop will run for the max value of y times"
