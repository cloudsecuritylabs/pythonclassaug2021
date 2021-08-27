
for x in range(6):
  print(x)

# for the sake of Python
# while we code
# Let's get this right!

# define a while loop
x = 0
while (x < 5):
    print(x)
    x = x + 1

# print in a single line
for x in range(5,10):
    print(x, end='')

counter = 0
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(counter, x)
  counter = counter + 1

# enumerate
for i,x in enumerate(fruits): # iterables
  print(i+1, x)

upperbound = 5
for i in range(1, upperbound + 1):
  print(i)

# # on strings
for x in "banana":
  print(x, end="*")

print()

for x in range(6):
  print(x, end=" ")

print()

num_list = [] # what if you change this to a tupple?
for x in range(6):
  num_list.append(x)
print(num_list)


num_list = [] # what if you change this to a tupple?
for x in range(6):
    if x==1:
        continue
        print("hello")
    else:
        num_list.append(x)
print(num_list)




