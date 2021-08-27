counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue # change to continue and break for demo
        print("passing {}".format(counter))

    else:
        print("The current number is: {}".format(counter))