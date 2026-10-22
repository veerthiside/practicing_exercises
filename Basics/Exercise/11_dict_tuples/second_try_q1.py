countries = {
    "china":143, 
    "india":136, 
    "usa": 32, 
    "pakistan": 21
}

command = input("Enter a command: ").strip().lower()
if command == "print":
    for country, population in countries.items():
        print(f"{country}==>{population}") 
elif command == "add":
    new_country = input("Enter the country name: ").strip().lower()
    if new_country in countries:
        print(f"{new_country} already exists.")
    else:
        population = int(input(f"Enter {new_country}'s population: "))
        countries[new_country] = population
        for country, population in countries.items():
                print(f"{country}==>{population}") 
elif command == "remove":
    to_remove = input("Enter the country to remove: ")
    if to_remove in countries:
        del countries[to_remove]
        for country, population in countries.items():
            print(f"{country}==>{population}")
    else:
        print(f"{to_remove} doesn't exists.") 
elif command == "query":
    country_name = input("Enter the country name you wanna query: ").strip().lower()
    the_population = countries[country_name]
    print(f"{country_name}==>{the_population}")
else:
    print("Unknown Command")