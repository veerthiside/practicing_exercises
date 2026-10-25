result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

heads = 0
tails = 0
for outcomes in result:
    if outcomes == "heads":
        heads = heads + 1
    elif outcomes == "tails":
        tails = tails + 1
    
print(f"Number of heads: {heads}.")

# why stuck?
# not able to count how many times heads came. - haha, so easy, the moment i wrote what i'm not able to do. i did it.





