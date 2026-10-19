india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter name of a famous city: ")

if city in india:
    print("This city belongs to India.")
elif city in pakistan:
    print("This city belongs to Pakistan.")
elif city in bangladesh:
    print("This city belongs to Bangladesh.")
else: 
    print("Not found. Try again with some other city name.")

