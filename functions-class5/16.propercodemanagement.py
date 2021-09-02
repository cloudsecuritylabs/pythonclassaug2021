import random
number = random.randint(1,5)

# print("Highly suspicious")

def main():
    for i in range(number):
        print("hello")
    not_main()
def not_main():
    print("interesting")


# print("interesting too")

if __name__ == '__main__': main()