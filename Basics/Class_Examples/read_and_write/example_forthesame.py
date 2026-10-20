# program to write in a file
new_file = open("C:\\Users\\asus\\Desktop\\itsMagic.txt", "w") # w for writing

new_file.write("Haha, do you see the magic?")

# append text
new_file = open("C:\\Users\\asus\\Desktop\\itsMagic.txt", "a") # a for appending
new_file.write("\nIsn't it so cool?")


# read the file
new_file = open("C:\\Users\\asus\\Desktop\\itsMagic.txt", "r") # r for reading
print(new_file.read())
new_file.close() # NEVER FORGET THIS
