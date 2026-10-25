# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

for km in range(1, 6):
    print(f"You have completed {km} km of race.")
    tired = input("Are you tired? yes/no: ").strip().lower()
    if tired == "yes" and km != 5:
        print("you didn't finish the race")
        break
    elif tired == "no" and km != 5:
        continue
    elif km == 5:
        print("Congratulations you finished the race!!")