# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.


# IMPORTANT every module with functions with keywords MUST be imported here (and AFTER the KWData import)
from data import *
from generalFunctions import *
from greetings import *
from userDetails import *
from currencyConverter import *
from TwitterAPI import *
from Translation import *


# the following function is where you add each function you create along with its keywords list.
# Just follow the existing pattern. (with elifs! please leave "else" as is)
def functionCheck(KWList, inputKeywords):
    # Function is meant to take in the selected list (on keywordsListSelection's output)
    # Function also takes in a list of input keywords, in case other inner functions need those.
    # Function then runs the function corresponding to the keywords list.

    if KWList == greetingsGeneralKWList:
        greetingsGeneral()
    elif KWList == showUserDetailsKWList:
        showUserDetails()
    elif KWList == replyToOkKWList:
        replyToOk()
    elif KWList == goodbyeKWList:
        goodbye()
    elif KWList == replyToLolKWList:
        replyToLol()
    elif KWList == replyToCritiqueKWList:
        replyToCritique()
    elif KWList == ccStartupKWList:
        ccStartup()
    elif KWList == GetTwitterJokeKWList:
        GetTwitterJoke()
    elif KWList == TranslationKWList:
        Translation()
    else:
        noInputMatch()


def keywordsListSelection(keywords):
    """Takes the keywords from user input and outputs the lists corresponding to each function that has the most matches."""
    countList = []

    # lowercase all keywords
    for i in range(len(keywords)):
        keywords[i] = keywords[i].lower()

    for i in range(len(keywordsList)):

        # lowercase all elements in keywordsList
        for m in range(len(keywordsList[i])):
            if not checkInputNumber(keywordsList[i][m]):  # A value will only be lower cased if it's not a number.
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
            if countListMax == 0:
                return [], keywords
            else:
                return keywordsList[i], keywords  # List of keywords equivalent to the most matched list of keywords (with the latter relating to a certain function)


def functionRun():
    """Function gets input from user and runs the most adequate function"""
    KWList, KWInput = keywordsListSelection(stringToKeywords(getUserInput()))
    functionCheck(KWList, KWInput)


def noInputMatch():
    outList = ["I'm sorry, but I didn't understand what you said. Please express yourself in other words.",
               "Apologies, but I didn't quite pick that up. Please rephrase.",
               "Sorry, but I don't know how to respond to that. Please tell it to me in other words."]
    print(outList[random.randint(0, len(outList) - 1)])
    functionRun()
