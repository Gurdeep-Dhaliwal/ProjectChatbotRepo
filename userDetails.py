# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# In case of anyone else's contribution, such should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

from data import *
import generalFunctions
from UserDatabase import *

try:
    userDetailsList = GetUser()
except:
    userDetailsList = []
# 0 = name
# 1 = age
# 2 = gender
# 3 = nickname


def getUserDetails():
    """Gets the user's personal data"""
    userDetailsList.append(getUserName())
    userDetailsList.append(getUserAge(0))
    userDetailsList.append(getUserGender(0))
    userDetailsList.append(getUserNickname())

    InputUser(userDetailsList)



def getUserNickname():
    print("Tell me your nickname.")
    nickname = str(generalFunctions.getUserInput())

    if generalFunctions.denial(nickname):
        print("Ok, you're in charge. Moving on...\n")
        return ""

    return nickname


def getUserName():
    """Function asks the user to input his/her name and outputs it"""
    print(end="" + "Please tell me your first name.")

    name = str(generalFunctions.getUserInput())

    # if executed, returns input as "None" and terminates function.
    if generalFunctions.denial(name):
        print("Ok, you're in charge. Moving on...\n")
        return ""

    name = generalFunctions.stringToCharacters(name)
    name[0] = name[0].upper()

    for letter in range(1, len(name)):
        name[letter] = name[letter].lower()

    return ''.join(name)

def getUserAge(n):
    """Gets the user's age and outputs it"""
    # ALWAYS run with input 0

    print(end="" + "How old are you?")

    age = generalFunctions.getUserInput()

    if generalFunctions.denial(age):
        print("Ok, you're in charge. Moving on...\n")
        return str("")

    if generalFunctions.checkInputNumber(age):
        return age
    else:
        if n < 1:
            print("Please express your age as a number.")
            n = n + 1
            return getUserAge(n)
        else:
            print("Don't make a fool of me... let's just move on...\n")
            return str("")


def getUserGender(n):
    """Gets the user's gender and outputs it"""
    # ALWAYS run with input 0

    print(end="" + "What is your gender?")

    gendersList = ["male", "female", "fluid", "gender fluid"]

    gender = str(generalFunctions.getUserInput())

    if generalFunctions.denial(gender):
        print("Ok, you're in charge. Moving on...\n")
        return ""

    if not generalFunctions.checkInputNumber(gender):
        gender = gender.lower()

    genderValidity = False
    for validGender in gendersList:
        if gender == validGender:
            genderValidity = True

    if generalFunctions.checkInputNumber(gender) or not genderValidity:
        if n < 3:
            print("That is not a gender... Are you trying to fool me?")
            n = n + 1
            return getUserGender(n)
        else:
            print("Don't make a fool of me... let's just move on...\n")
            return str("")
    else:
        if gender == "fluid":
            return "gender " + gender
        else:
            return gender


showUserDetailsKWList = ["About", "Know", "Details", "User"]
keywordsList.append(showUserDetailsKWList)
def showUserDetails():
    """Function prints the details the user has already given to the chatbot"""
    keywordsList.append(showUserDetailsKWList)

    count1 = len(userDetailsList)
    for i in range(len(userDetailsList)):
        if userDetailsList[i] == "" or userDetailsList[i] is None:
            count1 = count1 - 1

    if count1 == 0:
        print("I know nothing about you.")
    else:
        if count1 == 1 and userDetailsList[0] != "" and not (userDetailsList[0] is None):
            print("Rafael, at the moment, all I know is your name.")
        elif userDetailsList[0] != "" and not (userDetailsList[0] is None):
            print(end="" + "\n" + userDetailsList[0] + ", I already know that ")
        else:
            print(end="" + "\nAt the moment I know that ")

        count = 0
        for i in range(1, len(userDetailsList)):

            if userDetailsList[i] is None or userDetailsList[i] == "":
                count = count + 1
                continue

            print(end="" + "you are " + str(userDetailsList[i]))
            if i == len(userDetailsList) - 1:
                print(".")

            if i < len(userDetailsList) - 1:
                if i + 1 == len(userDetailsList) - 1 and (userDetailsList[i + 1] is None or userDetailsList[i + 1] == ""):
                    print(".")
                    break

                if userDetailsList[i + 1] != "" and not (userDetailsList[i + 1] is None):
                    # if i + 1 < (len(userDetailsList) - count):
                    print(end="" + ", and that ")
                else:
                    print(end="" + ".")


