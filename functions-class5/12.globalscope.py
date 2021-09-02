# explain the scope of a variable
# what is going to be printed here?
# everything that happens within a function, stays within a function
name = "dani"
def say_hi():
    # name = "Peter"
    x=10
    print("Hi {} ".format(name))


say_hi()


# help(say_hi)
#
# # name = "Peter"
# print(name)
#
