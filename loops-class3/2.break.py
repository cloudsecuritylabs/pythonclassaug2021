counter = 0
while counter < 10:
 counter += 1
 if counter == 7:
     print("found my match! stop searching!!")
     break
 else:
    print("The square root of {} is: {}".format(counter, counter * counter))


counter = 0
while counter < 10:
 counter += 1
 if counter == 7:
     print("I hate 7, skip square rooting!")
     continue
 else:
    print("The square root of {} is: {}".format(counter, counter * counter))


list_color = ["red", "yellow", "pink", "black"]
for color in list_color:
    if color == "pink":
        print("Found my match {}".format(color))
        break
    else:
        print("Looking! {} is not my matching color".format(color))