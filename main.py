# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

from generalFunctions import *
from greetings import *
from userDetails import *
import random

# the following is a two-dimensional array.
# each of the indexes in the first dimension corresponds to a list of keywords related to a certain function / feature.
# each of the indexes in the second dimension corresponds to the values (keywords) inside the listed lists for each function / feature.
# all keywords lists are named <functionName>KWList.
# To find which index your function's list corresponds to, just write keywordList.index()
keywordsList = [greetingKWList]


# The function body below was partially copied from a pynative.com article.
# link: https://pynative.com/python-check-user-input-is-number-or-string/
def checkInputNumber(uInput):
    """Returns True if the input is a number"""
    try:
        val = float(uInput)
        return True  # The print functions were removed and the function now returns a bool.
    except ValueError:
        return False  # The print functions were removed and the function now returns a bool.


def stringToKeywords(input):
    """Gets a string as an input and outputs it in a list of keywords"""
    return input.split()


def keywordsListSelection(keywords):
    """Takes the keywords from user input and outputs the lists corresponding to each function that has the most matches."""
    countList = []

    # lowercase all keywords
    for i in range(len(keywords)):
        keywords[i] = keywords[i].lower()

    for i in range(len(keywordsList)):

        # lowercase all elements in keywordsList
        for m in range(len(keywordsList[i])):
            keywordsList[i][m] = keywordsList[i][m].lower()

        countList.append(0)
        keywordsList[i].append(0)  # this adds an element which stores the number of keyword matches to the list being iterated over.
        count = 0  # counts every iteration of the inner loop.
        listLen = len(keywordsList[i])

        for keyW in keywords:

            count = count + 1
            if count > (listLen - 1):
                break

            if keyW in keywordsList[i]:
                countList[i] = countList[i] + 1
                keywordsList[i][-1] = keywordsList[i][-1] + 1  # adds 1 to the last element of the list being iterated over

    # I want it to go through each of the inner list's last element and retrieve the largest.
    countListMax = max(countList)

    for i in range(len(keywordsList)):
        if countListMax == keywordsList[i][-1]:
            del keywordsList[i][-1]
            return keywordsList[i]


def functionSelection(KWList):
    # Function is meant to take the selected list (on keywordsListSelection's output)
    # Function then runs the function corresponding to the keywords list.

    if KWList == greetingKWList:
        greeting()


# for j in range(len(keywordsList[0])):
#     keywordsList[0][j] = keywordsList[0][j].lower()

# print(keywordsList[0])

# testing thee whole thing
functionSelection(keywordsListSelection(stringToKeywords(getUserInput())))

# print(keywordsList[0][1])

# testList = [42, 75, 83, 24, 56]
# print(testList.index(max(testList)))


# The code below is meant to test the listed functions.
# introduction()
# showUserDetails()


# TEST checkInputNumber
# print(str(checkInputNumber("Eighteen")))
# print(str(checkInputNumber("18")))
