'''
Let's learn about list
'''

mixed_bag = ['blue', 22, [], {}, True, None, 22.2]

colors = ['red', 'blue']

# update a list
colors.insert(1, "yellow")

print(colors)
# delete item from a list
# TODO: what is the problem? uncomment line 15 to run into the issue!!
# del[colors[5]]
# list maintains it order


my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))
print(type(my_tuple))


# i need the first element
print(my_tuple[0])

# for the last element
print(my_tuple[4])
print(my_tuple[-1])
print(my_tuple[:])


# my_colors = ["red", "yellow"]
# my_colors.append("brown")
# my_colors.append("pink")
# print(my_colors)
# my_colors.insert(1, "blue")
# print(my_colors)
# my_colors.remove("blue")
# print(my_colors)


# # list.clear(1)
# # print(list)

