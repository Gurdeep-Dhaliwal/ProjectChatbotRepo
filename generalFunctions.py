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


# The function body below was partially copied from a pynative.com article.
# link: https://pynative.com/python-check-user-input-is-number-or-string/
def checkInputNumber(uInput):
    """Returns True if the input is a number"""
    try:
        val = float(uInput)
        return True  # The print functions were removed and the function now returns a bool.
    except ValueError:
        return False  # The print functions were removed and the function now returns a bool.
    