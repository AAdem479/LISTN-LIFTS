# unpacking a tuple practice

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# changing value, since tuples aren't updatable, might need to convert the tuple into a list

list_of_fruits = list(fruits)
# Access by index
list_of_fruits[1] = input("new fruit: ")

fruits = tuple(list_of_fruits)
print(fruits)

# I'll try with data type int

reps = (10, 11, 12)

reps_to_update = list(reps)
reps_to_update[0] = 11

# Before I print, expected output should be (11, 11, 12)
# must covert back to tuple first

reps = tuple(reps_to_update)

print(reps)

# Output: (11, 11, 12)