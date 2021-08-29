'''
print the error from an exception
we can respond with different messages based on type of error encountered
'''
num1=input("Enter first number: ")
num2=input("Enter second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    div = num1/num2
    print(div)

except ZeroDivisionError as error:
    print("Cant divide by Zero")
    print(f"this is the system message - > {error}")

except ValueError as error:
    print("Enter a number please , no strings allowed")
    print(f"this is the system message - > {error}")

except Exception as error:
    print(f"this is the system message - > {error}")
