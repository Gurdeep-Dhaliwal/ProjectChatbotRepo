# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

import userDetails
import random

greetingStartupKWList = ["Hello", "Hey", "Hi", "Hi-ya", "Hola"]

greetingsList = ["Hello", "Hey", "Hi", "Hi-ya", "Hola", "BANANA"]


def introduction():
    """Function presents the robot to the user, and might also collect their username."""
    # NOTE: ONLY run this is the user still hasn't provided his name.
    print("Hello, my name is KITT, I’m your personal assistant. ")
    userDetails.getUserDetails()
    print("Nice to meet you! From now on I’ll call you " + str(userDetails.userDetailsDict["name"]) +
          ". \nIf you ever wish to change the way I call you, just ask me to change your name.")


def greetingStartup():
    """Greets the user upon startup"""
    # NOTE: ONLY run this if the user has already provided his name.
    choiceListA = [", how may I help?", ", KITT's here for you, what do you need?", ", go straight to the point, I'm hungry",
                   ", I'm listening.", ", what do you want now? I demand sleep!"]

    greetingChoice = greetingsList[random.randint(0, len(greetingsList))]
    choiceA = choiceListA[random.randint(0, len(choiceListA))]

    print(greetingChoice + userDetails.userDetailsDict["name"] + choiceA)


greetingStartup()