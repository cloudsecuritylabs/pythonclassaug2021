
# Simple loop over a list
names = ['Dave', 'John', 'Ben', 'Jud', 'Baby']

#
# for name in names: # what if I change name to spiderman?
#     print(name)
# else:
#     print("All names were printed in the loop!")


# # Simple loop over a tuple
# names_tuple = ('Dave', 'John', 'Ben', 'Jud', 'Baby')
# for name in names_tuple:
#     print(name)
# else:
#     print("All names were printed in the tuple!")

# breaking out of a loop with conditionals
names = ['Ben','Dave', 'John', 'Jud', 'Baby']
for name in names:
    if name == 'Ben':
        continue #continue, pass
    print(name)

#print("All names were printed!")

#
# # printing partial loops
# fruits = ["Watermelon", "Banana", "Apple", "Pineapple", "Strawberry"]
# for fruit in fruits:
#     print(fruit)
#
# colors = ["Red", "Blue", "Green", "Yellow", "Grey"]
# for color in colors[1:4]:
#     print(color, end=" ")
#
# print()
# # While loops
# counter = 0
# while counter <= 3:
#     counter += 1       # note the use of counter # what if we comment out this line?
#     print(counter)
#
#
# # While loops
# counter = 0
# while counter <= 3:
#     print(counter)
#     counter += 1
