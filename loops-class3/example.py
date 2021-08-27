x = input("Enter a number")

cont = True

while cont:
    if type(x) != int:
        continue
    else:
        print(int(x) * int(x))
        break

