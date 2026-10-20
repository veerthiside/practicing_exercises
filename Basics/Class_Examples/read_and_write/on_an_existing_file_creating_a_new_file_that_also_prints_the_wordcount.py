# create a new file
file = open("C:\\Users\\asus\\Desktop\\file.txt", "w")
file.write("This is a new file.")
file = open("C:\\Users\\asus\\Desktop\\file.txt", "a")
file.write("\nThis is a new line on the same new file.")

file = open("C:\\Users\\asus\\Desktop\\file.txt", "r")
new_file = open("C:\\Users\\asus\\Desktop\\new_file.txt", "w")
for line in file:
    words = line.split(' ')
    new_file.write("Wordcount: "+str(len(words))+' · '+line)

new_file = open("C:\\Users\\asus\\Desktop\\new_file.txt", "r")
print(new_file.read())
file.close()
new_file.close()

