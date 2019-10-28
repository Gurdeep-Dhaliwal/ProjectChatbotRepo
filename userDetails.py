# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

import generalFunctions


userDetailsDict = {
    "name": "",
    "age": "",
    "gender": ""
}




def getUserDetails():
    """Gets the user's personal data"""
    userDetailsDict["name"] = getUserName()
    userDetailsDict["age"] = getUserAge()
    userDetailsDict["gender"] = getUserGender()


def getUserName():
    """Function asks the user to input his/her name and outputs it"""
    print(end="" + "May you please tell me your name?")
    return generalFunctions.getUserInput()


def getUserAge():
    """Gets the user's age and outputs it"""
    print(end="" + "How many years old are you?")
    return generalFunctions.getUserInput()


def getUserGender():
    """Gets the user's gender and outputs it"""
    print(end="" + "What is your gender?")
    return generalFunctions.getUserInput()


def showUserDetails():
    """Function prints the details the user has already given to the chatbot"""
    if userDetailsDict["name"] != "":
        print(end="" + "\nHello " + userDetailsDict["name"] + ", I already know that ")
    else:
        print(end="" + "\nHello, at the moment I know that ")

    userDetailsList = generalFunctions.dictToList(userDetailsDict)
    for i in range(1, len(userDetailsList)):
        print(end="" + "you are " + str(userDetailsList[i]))

        if i + 1 < len(userDetailsList):
            print(end="" + ", and that ")
        else:
            print(end="" + ".")
