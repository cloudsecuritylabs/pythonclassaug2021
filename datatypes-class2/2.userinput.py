'''
User input - they are always received as a string unless converted (casting)!
'''

name = input("Please enter your name \n")
age = int(input("please enter your age \n"))
height = input('Please enter your height \n')

print(name)
print(age) # "100"
print(height) # "5"

print(type(name))
print(type(age))
print(type(height))

#TODO: fix error
if (age) < 100:
    print("You are too young!")


