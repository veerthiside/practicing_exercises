indian = ["samosa", "litti", "naan"]
chinese = ["egg roll", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name: ")
if dish in indian:
    print("It's an indian dish.")
elif dish in chinese:
    print("It's a chinese dish.")
elif dish in italian:
    print("It's an italian dish.")
else:
    print("No idea. Try again with some famous dish names.")