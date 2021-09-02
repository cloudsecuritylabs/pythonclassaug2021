'''
random generates a random float number between 0.0 and 1.0
'''

import random
import datetime

# # prints a random value from the list
# list1 = [1, 2, 3, 4, 5, 6]
# print(random.choice(list1))

# # prints a random item from the string
# string = "greatclass"
# print(random.choice(string))
#
# using randrange() to generate in range from 20
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting.
# print("A random number from range is : ", end="")
# print(random.randrange(20, 50, 3))
# #
# random():- This method is used to generate a float random
# number less than 1 and greater or equal to 0.
# Python code to demonstrate the working of
# random() and seed()
#
# using random() to generate a random number
# between 0 and 1
print("A random number between 0 and 1 is : ", end="")
print(int(random.random() * 100))
#
# using seed() to seed a random number
random.seed(5)
#
# printing mapped random number
print("The mapped random number with 5 is : ", end="")
print(random.random())

# using seed() to seed different random number
random.seed(datetime.datetime.now())

# printing mapped random number
print("The mapped random number with 7 is : ", end="")
print(random.random())

# using seed() to seed to 5 again
random.seed(5)

# printing mapped random number
print("The mapped random number with 5 is : ", end="")
print(random.random())

# using seed() to seed to 7 again
random.seed(7)

# printing mapped random number
print("The mapped random number with 7 is : ", end="")
print(random.random())

# https://docs.python.org/3/library/random.html
# randrange(a, b+1)
random.randint(1, 10)

