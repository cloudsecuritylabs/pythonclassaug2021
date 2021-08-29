'''
You can create your own exception
'''
age = 13
try:
    if age < 18:
        raise Exception("the user is younger than 18")
except Exception as error:
    print(f"error - {error}")

