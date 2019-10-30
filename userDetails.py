# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

import generalFunctions

userDetailsList = []
# 0 = name
# 1 = age
# 2 = gender


def getUserDetails():
    """Gets the user's personal data"""
    userDetailsList[0] = getUserName()  # CHANGE
    userDetailsList[1] = getUserAge()  # CHANGE
    userDetailsList[2] = getUserGender()  # CHANGE


def getUserName():
    """Function asks the user to input his/her name and outputs it"""
    print(end="" + "Please tell me your name.")
    return generalFunctions.getUserInput()


def getUserAge():
    """Gets the user's age and outputs it"""
    print(end="" + "How many years old are you?")
    return generalFunctions.getUserInput()


def getUserGender():
    """Gets the user's gender and outputs it"""
    print(end="" + "What is your gender?")
    return generalFunctions.getUserInput()

showUserDetailsKWList = ["About", "Me", "Know", "Details", "User"]
def showUserDetails():
    """Function prints the details the user has already given to the chatbot"""
    if userDetailsList[0] != "":
        print(end="" + "\nHello " + userDetailsList[0] + ", I already know that ")
    else:
        print(end="" + "\nHello, at the moment I know that ")

    for i in range(1, len(userDetailsList)):
        print(end="" + "you are " + str(userDetailsList[i]))

        if i + 1 < len(userDetailsList):
            print(end="" + ", and that ")
        else:
            print(end="" + ".")
