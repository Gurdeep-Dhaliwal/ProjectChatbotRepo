# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

from generalFunctions import *
from greetings import *
from userDetails import *
import random
from PickleFileHandling import *

# the following is a two-dimensional array.
# each of the indexes in the first dimension corresponds to a list of keywords related to a certain function / feature.
# each of the indexes in the second dimension corresponds to the values (keywords) inside the listed lists for each function / feature.
# all keywords lists are named <functionName>KWList.
# To find which index your function's list corresponds to, just write keywordList.index()
keywordsList = [greetingsGeneralKWList]


def stringToKeywords(input):
    """Gets a string as an input and outputs it in a list of keywords"""
    return input.split()


def keywordsListSelection(keywords):
    """Takes the keywords from user input and outputs the lists corresponding to each function that has the most matches."""
    # keywordsList = FileRead("KeyWordsFile")

    kwl = keywordsList
    countList = []

    # lowercase all keywords
    for i in range(len(keywords)):
        keywords[i] = keywords[i].lower()

    for i in range(len(kwl)):

        # lowercase all elements in keywordsList
        for m in range(len(kwl[i])):
            kwl[i][m] = kwl[i][m].lower()


        countList.append(0)
        kwl[i].append(0)  # this adds an element which stores the number of keyword matches to the list being iterated over.
        count = 0  # counts every iteration of the inner loop.
        listLen = len(kwl[i])

        for keyW in keywords:

            count = count + 1
            if count > (listLen - 1):
                break

            if keyW in kwl[i]:
                countList[i] = countList[i] + 1
                kwl[i][-1] = kwl[i][-1] + 1  # adds 1 to the last element of the list being iterated over

    # I want it to go through each of the inner list's last element and retrieve the largest.
    countListMax = max(countList)

    for i in range(len(kwl)):
        if countListMax == keywordsList[i][-1]:
            del kwl[i][-1]
            return kwl[i]  # List of keywords equivalent to the most matched list of keywords (with the latter relating to a certain function)

    FileWrite("KeyWordsFile", kwl)


def functionCheck(KWList):
    # Function is meant to take in the selected list (on keywordsListSelection's output)
    # Function then runs the function corresponding to the keywords list.

    if KWList == greetingsGeneralKWList:
        greetingsGeneral()


def functionRun():
    """Function gets input from user and runs the most adequate function"""
    functionCheck(keywordsListSelection(stringToKeywords(getUserInput())))

# for j in range(len(keywordsList[0])):
#     keywordsList[0][j] = keywordsList[0][j].lower()

# print(keywordsList[0])

# testing thee whole thing
# functionCheck(keywordsListSelection(stringToKeywords(getUserInput())))

# print(keywordsList[0][1])

# testList = [42, 75, 83, 24, 56]
# print(testList.index(max(testList)))


# The code below is meant to test the listed functions.
# introduction()
# showUserDetails()


# TEST checkInputNumber
# print(str(checkInputNumber("Eighteen")))
# print(str(checkInputNumber("18")))
