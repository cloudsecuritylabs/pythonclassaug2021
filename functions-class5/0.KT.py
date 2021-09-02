my_dict = {"item1" : [1,2,3], "item2" : [10,12,13], "item3" : (100,121,131)}

x_tuple = (3,4,5)
my_dict["item1"].append(x_tuple)

for key,value in my_dict.items():
    print(key,value)