# is this function returngn anything?
def print_sum(num1, num2):
    sum = (num1+num2)
    print("the sum of {} + {} = {}".format(num1, num2, sum))
    return sum

number1 = int(input("enter first num? "))
number2 = int(input("enter second num? "))
print_sum(number1, number2)

# the NoneType comes back
print(type(print_sum(1,1)))