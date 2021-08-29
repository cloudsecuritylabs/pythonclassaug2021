'''
print the error from an exception
'''
try:
    num1 = 10
    num2 = "two"
    div = num1/num2
    print(div)
except Exception as error:
    print("Problem identified")
    print(f"the follow is system message - > {error}")

# if True:
#     print("i can code whatever i want")

