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


z = "35.5"

print("The last letter standing " + z)


# z = 35.5
#
# print("The last letter standing " + z)


with open("secret_file.txt", "w") as file:
    file.write("My secret password: P@ssw0rd123")

# uncomment to see infinite loop
# char_list = ["a", "b", "c", "d"]
# for char in char_list:
#     char_list.append(char)
#     print(char)

# secret best class ever
for i in range(3, 14, 5):
    if i == 13:
        shout = "best class ever!!"
        print(shout)



my_dict1 = [{"first_name"}, {"Ankan"}, {"last_name"}, "Basu"]
my_dict2 = {"first_name": "Ankan", "last_name": "Basu"}
my_dict3 = {"first_name:Ankan", "last_name:Basu"}
my_dict4 = ["first_name:Ankan", "last_name:Basu"]
my_dict5 = ("first_name:Ankan", "last_name:Basu")

print(type(my_dict1))
print(type(my_dict2))
print(type(my_dict3))
print(type(my_dict4))
print(type(my_dict5))



hi = None
print(hi)


print(type(4))

# can you unbind a variable from the current namespace?
# hi = "You are very smart"
# del hi
# print(hi)


# Python variables are not deeply linked
x = 10
y = x
x = 15
print(f'x is {x} and y is {y}')


# a,b,c = 1,2
# print(b)


name, age = input("Enter your name: "), input("Enter your age ")
print(f'your name is {name} and age is {age}')