'''
else and finally
talk about using break points
'''
try:
    num1 = 10
    num2 = 0 # change this to 0
    sum = num1/num2
    print(sum)
except ZeroDivisionError as error:
    print("Cannot divide by zero")
except Exception as error:
    print(f"general error - {error}")
else:
    print("no error occurred")
finally:
    print("this run always")