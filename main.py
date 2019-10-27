# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

from generalFunctions import *
from greetings import *
from userDetails import *

# the following is a two-dimensional array.
# each of the indexes in the first dimension corresponds to a list of keywords related to a certain function / feature.
# each of the indexes in the second dimension corresponds to the values (keywords) inside the listed lists for each function / feature.
# all keywords lists are named <functionName>KWList.
# To find which index your function's list corresponds to, just write keywordList.index()
keywordsList = [[greetingStartupKWList]]


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


def keywordsSelection(keywords):
    """Takes the keywords from user input and decides which of the chatbot's features should be executed"""
    countList = []
    countDict = {}

    for i in range(len(keywordsList)):

        # Need to get the size of the list to be iterated over
        # create an if to exit the 2nd loop in case it goes over the list's size.
        # (this will involve adding a count variable to inner loop)
        # get a randint() to get a random int between the size of the list being iterated over.
        # get to compare the keywords to the 2nd dimension of the list corresponding to the new int's index

        for keyW in keywords:


            if keywords[keyW] in keywordsList[i]:
                countList[i] = countList[i] + 1



































# The code below is meant to test the listed functions.
introduction()
showUserDetails()


# TEST checkInputNumber
# print(str(checkInputNumber("Eighteen")))
# print(str(checkInputNumber("18")))
