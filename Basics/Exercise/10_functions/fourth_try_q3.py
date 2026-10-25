# ⭐⭐⭐
# SEE THIS TRY. YOU UNDERSTOOD THIS QUESTION HERE.

# for i in range(4):
#     print("*")

# for i in range(5):
#     print("*", end="")

# n = 3
# for line in range(1, n+1):
#     for star in range(line): # for line = 1, it will run 1 time. for line = 2 it will run 2 times. for line = 3 it will run 3 times. line = 4 not possible coz range(1, 4).
#         print("*", end="")
#     print()

def print_pattern(size):
    for line in range(1, size+1):
        for star in range(line):
            print("*", end="")
        print()


pattern_size = int(input("Enter the size of the pattern: "))
print_pattern(pattern_size)


# You had to write it in this way:
# for line in range(1, n+1):
#     for star in range(line): # for line = 1, it will run 1 time. for line = 2 it will run 2 times. for line = 3 it will run 3 times. line = 4 not possible coz range(1, 4).