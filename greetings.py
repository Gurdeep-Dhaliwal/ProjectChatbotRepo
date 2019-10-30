# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

import userDetails
import random



# Write general introduction which decides which of the functions below to run depending on if name has been provided or not.
greetingsGeneralKWList = ["Hello", "Hey", "Hi", "Hi-ya", "Hola", "Heya", "Howdy"]
def greetingsGeneral():

    if 0 == len(userDetails.userDetailsList):  # Checks if the userDetailsList isn't empty.
        for i in range(3):
            userDetails.userDetailsList.append("")
        introduction()
    else:
        greeting()

    #if userDetails.userDetailsList[0] is None:
    #
    #else:
    #    greeting()


def introduction():
    """Function presents the robot to the user, and might also collect their username."""
    # NOTE: ONLY run this is the user still hasn't provided his name.
    print("Hello, I’m your personal assistant. ")
    userDetails.getUserDetails()
    print("Nice to meet you! From now on I’ll call you " + str(userDetails.userDetailsList[0]) +
          ". \nIf you ever wish to change the way I call you, just ask me to change your name.")


def greeting():
    """Greets the user upon startup"""
    # NOTE: ONLY run this if the user has already provided his name.
    greetingsList = ["Hello ", "Hey ", "Hi ", "Hi-ya ", "Hola ", "Heya ", "Howdy "]
    choiceListA = [", how may I help?", ", I'm here for you, what do you need?", ", go straight to the point, I'm hungry",
                   ", I'm listening.", ", what do you want now? I demand sleep!", ", be concise on what you want, or I'll go BANANA!!!"]

    greetingChoice = greetingsList[random.randint(0, len(greetingsList) - 1)]
    choiceA = choiceListA[random.randint(0, len(choiceListA) - 1)]

    print(greetingChoice + userDetails.userDetailsList[0] + choiceA)
