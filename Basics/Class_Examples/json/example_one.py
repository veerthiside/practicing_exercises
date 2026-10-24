book = {}

book ["tom"] = {
    "name": "tom",
    "address": "1 red street, NY",
    "phone": 12121212
}
book ["bob"] = {
    "name": "bob",
    "address": "1 blue street, NY",
    "phone": 21212121
}

import json
s = json.dumps(book) # s in dumps converts it in string then it it converted into json format
# print(s)
with open("Basics//Class_Examples//json//book.txt", "w") as f:
    f.write(s) 