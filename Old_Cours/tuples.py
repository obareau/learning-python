# create a tuple
high_score = ("Nimish", 120)
print(high_score)

# reassign the entire tuple
high_score = ("Holly", 150)
print(high_score)

# modifying individual elements of a tuple is not allowed
# high_score[0] = "fadsfsd"

# retrieve the value at an index of a tuple
name = high_score[0]
print(name)

# get the length of the tuple
print(len(high_score))

# check if an element exists in a tupel or a list
does_contain = "Holly" in high_score
print(does_contain)

# applying some of the above logic to strings
# retrieve the first letter of a string
print(name[0])

# retrieve a range of letters of a string
print(name[0:2])

# check if the string contains a substring
print("Hol" in name)

# get the length of the string
print(len(name))