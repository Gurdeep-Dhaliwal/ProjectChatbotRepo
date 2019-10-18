# The following code has been developed by Rafael de Moura Afonso Rodrigues.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# This will be removed once everyone starts having a relevant contribution to this module.
# Then the contribution should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

"""Current "sub"features present in this file:
1. Introduction - the chatbot introduces itself to the user and asks for a few personal details. - DONE
2. Personal details - the chatbot presents the user's personal details in a "humanized" sentence. - DONE
3. During the introduction, the robot (whether the user wants it to or not) asks for more personal details. - TO DO"""

# Maybe not in this file, but I'd really like to do the part where there is a search for terms/synonyms, matching with contexts, etc
# This file/functions will adapt the user's input and grab keywords from it, compare them with other stored keywords.
# And many more things. A bit of an Ai thing ig. This will be helpful for every feature that anyone decides to implement.
# I'll make sure to include a brief text explaining how it works, and comments next to the main inputs/outputs.
# That way everyone will be able to use it however you want to.

# NOTES:

# @LEO, for all the things I'm trying right now, I'm using dictionaries / .txt and .cvs files.
# As I assume most people don't know databases, they will probably be doing the same for now.
# It'd be nice if at some point in time, with mutual agreement, you could go over those things and try to store them in databases.
# Obviously when doing this don't forget to add a comment saying you did it, next to the other person's code.

# @GURDEEP, when you can, please create one of those azure devops thinguies for the features / tasks etc.
# These "subfeatures" I listed could be elements of that for example.
# The features in the presentation, as they are more general, could stand on a higher level in the devops thign.

# @EVERYONE, tomorrow (17(ops, 18)/10), I'll make sure to get the git fully working.
# I'll write a document with straight to the point instructions o how to work with GIT through the Windows commandline.
# It REALLY is the most uniformized way to work, and once you mechanize the commands there isn't a lot of margin for error.
# This way we can start working at full gas without risking overlappig each others work, which can easily happen and it sucks.


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


