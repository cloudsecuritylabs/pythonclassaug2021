'''
Types of functions
1. Basic function
2. Funtion with parameters
3. Funtion with return values

   Built-in functions
        print()
        input()
    User-defined functions
        def something_new()
TODO: remember to call a function
'''
import datetime

def basic_function():
    print("I am a basic function without any parameters")
    # nothing to return

def function_with_parameters(parameter1, parameter2):
    sum = parameter1 + parameter2
    print("the sum of 2 paramter is {}".format(sum))
    # nothing to return

def funtion_with_return_values(parameter1, parameter2):
    sum = parameter1 + parameter2
    return sum
    # this will return the "sum"

## you must call a function!!!


def greetings():
    name = input("Enter your name: ")
    print("Welcome, {}!".format(name))

# greetings()

# scope of a funtion can be within another function
def get_time():
    # greetings()
    currentTime = datetime.datetime.now()
    time_string = currentTime.strftime("%H:%M:%S")
    print("current time {}".format(time_string))

get_time()


