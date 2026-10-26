# Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line

street = "north street"
city = "heaven city"
country = "earth"

address = street + ", " + city + ", " + country
print(address)
address = f"{street}, {city}, {country}"
print(address)

# print(address.split(","))
for items in address.split(","):
    print(items.strip())