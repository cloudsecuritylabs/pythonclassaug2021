'''
Let's learn about dictionary
Order is NOT maintained!!!
'''
person = dict()
person['name'] = "Ankan Basu"
person['age'] = 100
person['phone'] = '999-999-9999'

# del person['age']
# person.clear()

for item, value in person.items():
    print(item, value)

#
#
# pet = dict()
# pet['name'] = "Watson"
# pet['age'] = 5
#
# print(pet)
#
#
# # update dictionary
#
# # delete items from a dictionary
#
# pet.clear()
# print(pet)