'''
Logical operator
'''
# AND, OR, XOR, NOT

is_sky_blue = False
is_cloudy = True

if (is_cloudy or is_sky_blue):
    print("Hey it could be raining")

# expand the concept, remove ==
if (is_cloudy == False & is_sky_blue == True):
    print("Hey could be raining")


# AND --> must evaluate both sides of the operator
# OR  --> not always true

num1 = "20"
num2 = 30

if (type(num1)== int and type(num2)==int):
    print(True)

num1 = 20
num2 = "student"
if (type(num1)== int or type(num2)==int):
    print(True)

# binary operators
print(100>100)
