# The 'requests' module is used to make requests to API's online
import requests,json
from generalFunctions import *


def TranslateText(Text, Language):
    # Function to translate the given text under the argument Text to the language given under the argument Language.
    # The Language given is converted to its language code which is then passed to a translation API with the Text.
    # The function then returns the data returned by the API.
    # If the function encouters any errors whilst translating,
    # it will return a string informing the user that there was an error and prompt them to check their formatting of the arguments.

    if True:
        Key="trnsl.1.1.20191105T220926Z.e747b96073e3c078.eaa300fca7f8ec15dbe6b87c84bc08925108275c"
        Parameters={"lang":LanguageCodes[Language.lower()],"key":Key,"text":Text,"format":"plain"}
        Request=requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate",params=Parameters)
        JsonData=Request.json()
        return JsonData["text"][0]
    else:
        return "Unknown Error Translating. Please check formatting of inputs."


def getLanguage(p):

    print("Which language do you wish to translate to?")

    language = getUserInput()
    language = language.lower()

    if language not in list(LanguageCodes.keys()) and p <= 2:
        print("Sorry, that is not a valid language... check your typing, please :3")
        return getLanguage(p+1)
    elif language not in list(LanguageCodes.keys()) and p > 2:
        print("Ok clearly your brain is not working atm. Let's move on.")
        return("noLanguage")
    else:
        return language

def getText():

    print("Please type the text you wish to translate.")
    return getUserInput()


TranslationKWList = ["translate","decipher"]
keywordsList.append(TranslationKWList)


def Translation():
    language = getLanguage(0)

    if language == "noLanguage":
        return ""

    text = getText()

    print(TranslateText(text, language))
