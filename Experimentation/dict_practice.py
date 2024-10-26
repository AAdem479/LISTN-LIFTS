# dictionary format practice

dict = {"water": "safia",
        "price": 2,
        "location": "monoprix",
        "consumer": "humans",
        "safe": True}

print(dict)

# access items

brand = dict["water"]
# print(brand)

# get keys, keys are the names and items in which hold the value.

keys = dict.keys()
# print(keys)

# get values of said keys

# values = dict.values()
# print(values)

# change value of key

## dict["price"] = 3  # inflation
dict["location"] = "Geant"
# dict["quality"] = "high"

# print(dict)

# Get items

items = dict.items()
# print(items)


# check if key is in the dictionary (important)

# if "price" in dict:
        # print("yup, 'price' is there")
# else:
        # print("nope 'price' ain't there")

dict["safe"] = False
print(dict)
