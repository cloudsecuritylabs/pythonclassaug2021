from datetime import datetime
def Greetings():
    name = input("Enter your name: ")
    print("Welcome, {}!".format(name))
    return name

def getTime():
    currentTime = datetime.now()
    time_string = currentTime.strftime("%H:%M:%S")
    print("current time {}".format(time_string))

def getUserNameAndEmail():
    mail = input("enter your mail please ? ")
    return mail

def printDetails():
    name = Greetings()
    mail = getUserNameAndEmail()
    print("\nuser details :")
    print("name : {}\nmail : {}".format(name,mail))
    getTime()

printDetails()