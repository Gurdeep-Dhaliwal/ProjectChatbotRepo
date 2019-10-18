# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

from generalFunctions import *
from introduction import *
from userDetails import *


# The function body below was partially copied from a pynative.com article.
# link: https://pynative.com/python-check-user-input-is-number-or-string/
def checkInputNumber(uInput):
    """Returns True if the input is a number"""
    try:
        val = float(uInput)
        return True  # The print functions were removed and the function now returns a bool.
    except ValueError:
        return False  # The print functions were removed and the function now returns a bool.


#The code below is meant to test the listed functions.
introduction()
showUserDetails()


# TEST checkInputNumber
# print(str(checkInputNumber("Eighteen")))
# print(str(checkInputNumber("18")))
