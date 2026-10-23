stock = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}

# print(stock["ril"])

while True:
    command = input("Enter a command: ").strip().lower()

    if command == "print":
        # print("You chose print.")
        for company, prices in stock.items():
            total = sum(prices)
            count = len(prices)
            average = total / count
            print(f"{company} ==> {prices} ==> avg:  {average:.2f}")
    elif command == "add":
        # print("You chose add.")
        company = input("Enter company's name: ").strip().lower()
        price = int(input("Enter its price: "))
        if company in stock: 
            stock[company].append(price)
        else:
            stock[company] = [price]
    elif command == "quit":
        break
    else:
        print("That operation doesn't exist. Try something else.")


"""
why stuck?
- how to call 600 from info? - this is not the way. 
- when doing "for company, stock_value in stock" it says too many values to unpack. - use .items() to print the dictionary
"""

