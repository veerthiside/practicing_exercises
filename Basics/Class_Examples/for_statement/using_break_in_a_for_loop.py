key_location = "closet"

locations = ["living room", "closet", "garage"]
for i in locations:
    if i==key_location:
        print("The key is found in", i)
        break
    else:
        print("The key is not found in", i)