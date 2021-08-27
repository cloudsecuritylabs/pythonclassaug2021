numlist = [10, 22, 44, 30]
for i in numlist:
    if numlist[0] > 6 and numlist[3] > 40:
        print("Both numbers are bigger")
    elif numlist[1] == 22 or numlist[2] == 60:
        print("One of the numbers is equal")
        break
    else:
        print("None of this is true")