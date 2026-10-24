file = open("Basics/Class_Examples/json/book.txt", "r")
read_file = file.read()
print(read_file)
print(type(read_file))

import json
book = json.loads(read_file) # json load string "read_file"
print(book)
print(type(book))


print(book['bob']['phone']) # from book dictionary print 'phone' of 'bob'

for details in book:
    print(book[details])