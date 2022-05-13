database = {}

import random

bal = 3000


def init():
    isValidOptionSelected = False
    print('Welcome To Bank Green')

    while isValidOptionSelected == False:

        haveAccount = int(input('Do You Have An Account With Us 1.(Yes) 2.(No) \n'))

        if (haveAccount == 1):
            isValidOptionSelected = True
            logjn()
        elif (haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print('You Have Selected An Invalid Option')
            init()


def register():
    print("********  Start Registration  *********")

    email = input("What is Your Email address? \n")
    first_name = input("What is Your First Name? \n")
    last_name = input("What is Your Last Name? \n")
    password = input("Create a Password \n")

    newAccountNumber = generateAccountNumber()

    database[newAccountNumber] = [first_name, last_name, email, password]

    print("Your Accoubt Has Been Created")
    print("== == == == == ==")
    print('Your Account Number is: %d' % newAccountNumber)
    print("Thank You For Creating An Account With Us")
    print("== == == == == ==")
    login()


def login():
    print("****** Login ******")


    userAccountNumber = int(input("Account Number \n"))
    password = input("Password \n")

    for newAccountNumber,userDetails in database.items():
        if (newAccountNumber == userAccountNumber):
            if (userDetails[3] == password):
                bankOperations(userDetails)

    print('Invalid Account Number or Password')

    login()


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def bankOperations(user):

    print("Welcome %s %s" % ( user[0], user[1] ) )
    print("1.Withdrawal")
    print("2.Deposit")
    print("3.Complaint")
    print("4.Logout")

    dashOptions = int(input("Select An Option \n"))

    if (dashOptions == 1):
        withdrawalOPtion()

    elif (dashOptions == 2):
        depositOption()

    elif (dashOptions == 3):
        complaintOption()

    elif (dashOptions == 4):
        logoutOption()


def withdrawalOPtion():
    print("You Selected Withdrawal")

    withOut = int(input("How much would you like to Deposit \n"))
    print("Balance")
    print(bal + withOut)


def depositOption():

    print("You selected Deposit")

    depIn = int(input("How much would you like to Deposit \n"))
    print("Balance")
    print(bal + depIn)


def complaintOption():
    print("You selected Complaint")

    customerComp = input("what issue would you like to report? \n")
    print("Thank you reaching Out To Us")
2

def logoutOption():
    init()


#### Actual System ####

init()
