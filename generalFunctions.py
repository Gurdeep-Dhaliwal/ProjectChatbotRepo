# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

"""Current "sub"features present in this file:
1. Introduction - the chatbot introduces itself to the user and asks for a few personal details. - DONE
2. Personal details - the chatbot presents the user's personal details in a "humanized" sentence. - DONE
3. During the introduction, the robot (whether the user wants it to or not) asks for more personal details. - TO DO"""


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


def ListToDictKeyKey(list, indexDType, valDType):
    """Function takes the INDEXES from a list and outputs them to a dictionary, where the INDEX is the SAME AS the VALUE.
    Have DType variables be true if you want the type stored to be an int, or false if you want it to be a string"""
    # Have in mind this function does not return any of the list's values, only it's indexes.

    listDict = {}
    objectDict = listDict
    for index in range(len(list)):

        if indexDType == True and valDType == True:
            objectDict.add(index, index)
        elif indexDType == True and valDType == False:
            objectDict.add(index, str(index))
        elif indexDType == False and valDType == True:
            objectDict.add(str(index), index)
        else:
            objectDict.add(str(index), str(index))

    return objectDict

# ListToDictKeyKey test
testList = [5, 7, 6, 2, 3]
testDict = ListToDictKeyKey(testList, True, False)
print(testDict)
