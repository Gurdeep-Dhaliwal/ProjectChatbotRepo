# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

import userDetails


def introduction():
    """Function presents the robot to the user, and might also collect their username."""
    print("Hello, my name is KITT, I’m your personal assistant. ")
    userDetails.getUserDetails()
    print("Nice to meet you! From now on I’ll call you " + str(userDetails.userDetailsDict["name"]) +
          ". \nIf you ever wish to change the way I call you, just ask me to change your name.")
