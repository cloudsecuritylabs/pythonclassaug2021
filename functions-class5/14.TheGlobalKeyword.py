name = "dani"

def callDani():
    # the global scope
    # be careful when usign global keyword
    # global name
    print("Hi {}".format(name))
    name = "Peter"

callDani()
print("Hi {}".format(name))