# ⭐⭐⭐ 

with open("Basics/Exercise/13_read_write_files/poem.txt", "r", encoding="utf-8") as file: # open the file at x location in reading mode which has encoding utf-8, calling it file in short
    text = file.read() # store the file in text variable

words = text.split() 
clean_words = []
for each_word in words:
    each_word = each_word.lower().strip(",.;:!?—")
    clean_words.append(each_word)

counts={}
for the_word in clean_words: # for each item in the list
    if the_word in counts: # if the item is in the dictionary
        counts[the_word] = counts[the_word] + 1 # increase the value of item by 1
    else:
        counts[the_word] = 1 # if not, give the item a value of 1


print(counts)
# print(clean_words)
# print(len(clean_words))

highest_count = max(counts.values()) # find the max value from the values of the dictionary 
# print(highest_count)

print("\nHighest Frequency:")
for the_word in counts: # for each key in the dictionary
    if counts[the_word] == highest_count: # if the value is equal to highest count
        print(the_word + " appeared " + str(highest_count) + " times") 