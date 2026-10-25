# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

each_km = [1, 2, 3, 4, 5]

for km in each_km:
    print(f"You have completed {km} km of the race.")
    ask = input("Are you tired? yes/no: ").strip().lower()
    if ask == "yes" and km != 5:
        print("you didn't finish the race")
        break
    elif ask == "no" and km != 5:
        continue
    elif ask == "no" and km == 5:
        print("Congratulations you finished the race!!")

# why stuck?
# - everything is working but at 5th km if the user says yes, program doesn't congratulate them. - solved in 2nd try.



        