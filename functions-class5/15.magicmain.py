'''
Most other programming languages require a special function, called main(),
which tells the operating system what code to execute when a program is invoked.
Python - it is not mandaroty but a good practice

if you use __name__, it will automatically be set to __main__


'''


import Welcome_Message
def main():
    print("this is the main File")
    print("welcome_message does not run")

if __name__ == '__main__': main()
