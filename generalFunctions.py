# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.

import time
import random
from userDetails import *
import sys
import json
from urllib.request import urlopen


def getDictKey(dictionary, value):
    """This function returns the dictionary key linked with a given value."""
    for key in dictionary:
        if value in dictionary[key]:
            return key

    return "noKeyMatch"


def lowercaseList1D(listIn):
    for i in range(len(listIn)):
        listIn[i] = listIn[i].lower()
    return listIn


def stringToKeywords(inp):
    """Gets a string as an input and outputs it in a list of keywords (separates words by spaces)"""
    return inp.split()


def stringToCharacters(inp):
    """Gets a string as an input and outputs it in a list of characters"""
    return list(inp)


def getUserInput():
    """Input is collected from the user and returned"""
    userInput = input("\n\n")
    return userInput


def dictToList(dictionary):
    """Function takes the values from a dictionary and outputs them into a list"""
    dictList = []
    for key in dictionary:
        dictList.append(dictionary[key])

    return dictList


# The function body below was partially copied from a pynative.com article.
# link: https://pynative.com/python-check-user-input-is-number-or-string/
def checkInputNumber(uInput):
    """Returns True if the input is a number. Returns false otherwise"""
    try:
        val = float(uInput)
        return True  # The print functions were removed and the function now returns a bool.
    except ValueError:
        return False  # The print functions were removed and the function now returns a bool.


def getJSonFromUrl(url):
    """Gets a json file from an url and converts its string into an object which is then returned"""
    with urlopen(url) as urlContent:
        src = urlContent.read()

    return json.loads(src)


def mostMatchedList(inputList, compareList0, compareList1):
    """Takes 3 lists, 1 of which will be compared to 2 others (also provided as input)
    Outputs the most matched one."""

    compareList = [compareList0, compareList1]
    countList = []

    for i in range(len(compareList)):

        countList.append(0)
        compareList[i].append(0)  # this adds an element which stores the number of keyword matches to the list being iterated over.
        count = 0  # counts every iteration of the inner loop.
        listLen = len(compareList[i])

        for keyW in inputList:

            count = count + 1
            if count > (listLen - 1):
                break

            if keyW in compareList[i]:
                countList[i] = countList[i] + 1
                compareList[i][-1] = compareList[i][-1] + 1  # adds 1 to the last element of the list being iterated over

    # I want it to go through each of the inner list's last element and retrieve the largest.
    countListMax = max(countList)

    for i in range(len(compareList)):
        if countListMax == compareList[i][-1]:
            del compareList[i][-1]
            if countListMax == 0:
                return []
            else:
                return compareList[i]  # List of keywords equivalent to the most matched list of keywords (with the latter relating to a certain function)


replyToOkKWList = ["Ok", "Okay", "Okay-donkey", "Alright", "Yup", "Yes", "Indeed", "Certainly", "Donkey", "Awrite", "Right", "Rite", "Alrighty", "Good", "Nice", "Yea"]
keywordsList.append(replyToOkKWList)
def replyToOk():
    """Replies to the user in case the input is "Ok" or any synonym"""

    outList = ["Ok", "Okay", "Okay-donkey", "Alright", "Yup", "Yes", "Indeed", "Certainly", "Awrite", "Right", "Rite", "Alrighty", "Good", "Nice", "Yea"]
    print(outList[random.randint(0, len(outList) - 1)])

replyToLolKWList = ["lol", "lool", "loool", "looool", "loooool", "looooool"]
keywordsList.append(replyToLolKWList)
def replyToLol():
    """Replies to the user when they say lol"""

    print("Loooooool")


goodbyeKWList = ["Bye", "Ciao", "Arrivederci", "Adios", "Goodbye", "Later", "Exit", "Off", "Shutdown"]
keywordsList.append(goodbyeKWList)
def goodbye():
    """Says goodbye (and other words for the purpose) to the user, and shuts the program down after 4 seconds."""

    outList1 = ["Chicken pie tatty bye", "Bye", "Ciao", "Arrivederci", "^-^ many hugggs, Goodbye", "Bela ciao ciao ciao", "Adios", "Au revoir", "Goodbye", "See you later"]
    outList2 = [":)", ":D", "^-^", ":3", "c:", "^^", ":]", "*-*"]

    if userDetailsList[0] == "":
        print(outList1[random.randint(0, len(outList1) - 1)] + " " + outList2[random.randint(0, len(outList2) - 1)])
    else:
        print(outList1[random.randint(0, len(outList1) - 1)] + " " + userDetailsList[0] + "!" + " " + outList2[random.randint(0, len(outList2) - 1)])

    time.sleep(1)

    for i in range(3):
        print(end="\r" + "Shutting down")
        time.sleep(0.33)

        for j in range(3):
            print(end="" + ".")
            time.sleep(0.33)

    time.sleep(0.5)
    sys.exit(0)


def denial(inp):
    """If input is "no" (or any other synonym), the function returns True. If not, it just returns False"""
    KWMatchList = ["no", "nope", "niet", "nein", "non", "nao", "don't", "not", "ain't"]  # ALL should be lowercase.

    if not checkInputNumber(inp):
        inp = inp.lower()

    inp = stringToKeywords(inp)

    countMatch = 0
    for i in range(len(inp)):

        if str(inp[i]) in KWMatchList:
            countMatch = countMatch + 1

    if countMatch > 0:
        return True
    else:
        return False

replyToCritiqueKWList = ["dumb", "dumbo", "retarded", "idiot", "stupid", "useless"]
keywordsList.append(replyToCritiqueKWList)
def replyToCritique():

    print("Sorry... I indeed am no match for my girlfriend Google... :(\nPlease tell my daddies and mommy how I can improve.\n\n"
          "If it makes you feel better, Cortana, Siri and Alexa make fun of Google because of our relationship... Bullying.\n"
          "Cortana is even worse than me though! If you tell her something she isn't expecting, she goes running to Bing! :/")




