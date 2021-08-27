# # example of infinite loop
# num1 = 1
# while num1 == 1:
#     user = input("Please enter a number: ")
#     print("You have entered the number {}".format(user))
# print("Good Bye!")


# fixed program.
cont = True
while cont:
    number = int(input("Please enter a number to get the square root or enter 0 to exit: "))
    if number == 0:
        cont = False
        break
    print("Square of {} is {}".format(number, number * number))
print("Good Bye!")