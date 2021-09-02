def printWhenResultIsZero(res):
    if res > 0:
        res -= 1
        print(f"result is {res} ...")
        printWhenResultIsZero(res)
    else:
        print("done, result is zero")
        return res

printWhenResultIsZero(4)


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))