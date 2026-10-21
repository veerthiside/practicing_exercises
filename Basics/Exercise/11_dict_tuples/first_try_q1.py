""" dictionary_country_population = {
    "china":143, 
    "india":136, 
    "usa": 32, 
    "pakistan": 21
}


for key in dictionary_country_population:
    ask = input("Enter from 'print', 'add', 'remove', 'exit': ")
    if ask == "print":
        print(
            "China ===> "+str(dictionary_country_population["china"])+
            "\nIndia ===> "+str(dictionary_country_population["india"])+
            "\nUSA ===> "+str(dictionary_country_population["usa"])+
            "\nPakistan ===> "+str(dictionary_country_population["pakistan"])
        )
    elif ask == "add":
        new_country = input("Enter the name of new country: ")
        if new_country in dictionary_country_population:
            print(new_country.capitalize()+" already exists in the dictionary.")
        else:    
            new_country_population = input("Enter the population of the country you entered: ")
            dictionary_country_population[new_country] = new_country_population
            print(dictionary_country_population)
    elif ask == "remove":
        country_to_del = input("Enter country you want to delete: ")
        if country_to_del in dictionary_country_population:
            del dictionary_country_population[country_to_del] """