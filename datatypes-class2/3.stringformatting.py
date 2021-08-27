'''
String formatting
'''
# string is an object!

my_string1 = "Hi I am John and I am 40 years old"
print(my_string1)

# old C type string formatting, not recommended with Python any more
my_string2 = "Hi I am %s and I am %d years old" % ('John1', 40)
print(my_string2)

my_string3 = "Hi I am {} and I am {} years old".format('John2', 44)
print(my_string3)

my_string4 = "Hi I am {} and I am {} years old".format('John', 40)
print(my_string4)

# python 3.5 or better
name = 'john4'
age = 50
my_string4 = f"Hi I am {name} and I am {age} years old. math {3*3}"
print(my_string4)

print(str(5) + ": five")