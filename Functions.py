import random

database = {
    2255735494: ["Swaleh", "Cosmas", "cosmas@gmail.com", "mypass", 0]
}

def init():
    print('Welcome to our bank')

    haveAccount = int(input("Do you have account with us: 1 (Yes) 2 (No) \n"))

    if haveAccount == 1:

        login()
    elif haveAccount == 2:

        register()
    else:
        print("You have selected wrong option")
        init()

def login():
    print("************ Login **********")

    accountNumberFromUser = int(input("Input your account number: \n"))
    password = input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == password:
                bankOperation(userDetails)
            else:
                print("Unauthorised")
        else:
            print("Invalid account or password") 
    login()

def register():
    print("***Welcome to register***")

    email = input("Indicate your email address: \n")
    firstName = input("What is your first name? \n")
    lastName = input("What is your last name? \n")
    password = input("Create a password you can remember \n")

    accountNumber = generatedAccountNumber()

    database[accountNumber] = [firstName, lastName, email, password]

    print("Congratulations your account has been created")
    print("----------------------------------")
    print("Your account number is: %d" %accountNumber)
    print("Keep your account number safe")
    print("----------------------------------")

    login()


def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selectedOption = int(input("Select banking service (1) Deposit (2) Withdraw (3) Logout (4) exit \n"))

    if selectedOption == 1:

        depositOperation()
    elif selectedOption == 2:

        withdrawalOperation()
    elif selectedOption == 3:

        logout()
    elif selectedOption == 4:

        exit()
    else:

        print("Select valid option please")
        bankOperation(user)

def withdrawalOperation():
    print("Withdrawal services")
    getCurrentBalance([4])
    amountNeeded = int(input("How much to withdraw: \n"))
    if getCurrentBalance([4]) > amountNeeded:
        newBalance = getCurrentBalance([4]) - amountNeeded
        print("Your balance is %d" % newBalance)
    else: 
        print("You have insufficient amount in your account")


def depositOperation():
    print("Deposit services")
    getCurrentBalance([4])
    amountDeposited = int(input("How much to deposit: \n"))
    newBalance = getCurrentBalance([4]) + amountDeposited
    print("Your current balance is %d," %newBalance)
    

def generatedAccountNumber():
    return random.randrange(1111111111, 9999999999)


def generateCurrentBalance ():
    return random.randrange(1000, 8888)


def setCurrentBalance(userDetails, balance):
    userDetails[4] = balance


def getCurrentBalance(userDetails):
    return userDetails[4]


def logout():
    login()


"""
Internal Banking System
"""

init()




     