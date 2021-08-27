print("-------------------------------------------------")
for x in "banana":
    print(x, end="*")
print()
print("-------------------------------------------------")

for x in range(6):
    print(x, end=" ")
print()
print("-------------------------------------------------")


num_list = [] # what if you change this to a tupple?
for x in range(6):
  num_list.append(x)
print(len(num_list))
print()
print("-------------------------------------------------")

counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        pass # change to continue and break for demo
        print("passing {}".format(counter))

    else:
        print("The current number is: {}".format(counter))
print()
print("-------------------------------------------------")

# this is an example of infinite loop you do not want to create
# counter = 0
# while(counter < 5):
#     print(counter)

colors = ["Red", "Blue", "Green", "Yellow", "Blue", "Grey"]
for color in colors[1:4]:
    print(color, end=" ")
print()
print("-------------------------------------------------")


list_color = ["red", "yellow", "pink", "black"]
for color in list_color:
    if color == "pink":
        print("Found my match {}".format(color))
        break
    else:
        print("Looking! {} is not my matching color".format(color))
print()
print("-------------------------------------------------")