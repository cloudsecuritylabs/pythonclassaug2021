def Print_Numbers(item_list):
    for item in item_list:
        if type(item) == int:
            print(item)
        else:
            if type(item) == list:
                Print_Numbers(item)

items = [1,2,"a",3,[4,"b",5,6],[7,[8,"c",9]]]

Print_Numbers(items)