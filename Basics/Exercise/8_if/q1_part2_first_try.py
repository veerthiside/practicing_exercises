india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter name of a famous city: ")
city2 = input("Enter name of an another famous city: ")

if city1 and city2 in india:
    print("Both the cities belongs to India.")
elif city1 and city2 in pakistan:
    print("Both the cities belongs to Pakistan.")
elif city1 and city2 in bangladesh:
    print("Both the cities belongs to Bangladesh.")
else: 
    print("Both the cities don't belong to same country according to the current database." \
    " Try again with some other city names.")