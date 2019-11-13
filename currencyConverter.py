import json
from urllib.request import urlopen
from data import *
from generalFunctions import *
from data import *

# The link in the code below was copied from an API's website.
# The links imported throughout this module can be found on the website below
# Link to API website: https://exchangeratesapi.io/
# with urlopen("https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&base=USD") as urlContent:
#    src = urlContent.read()
# end of copied code

# jsonContentObj = json.loads(src)
# jsonContentStr = json.dumps(jsonContentObj["rates"]["2018-05-04"], indent=4)  # the dictionary was converted to a list for readability.
# print(jsonContentStr)
# print(jsonContentObj["rates"]["CAD"])  # Example of how to retrieve data



def getFromCurrency(n):
    """Function takes as input:
    1. Int number 0 (for technical purposes)
    Function outputs:
    1. A the currency code, eg. "EUR", the user wants to convert from
    """

    print("Which currency do you wish to convert from?")
    inputKWs = lowercaseList1D(stringToKeywords(getUserInput()))  # Gets input string from user, stores all words in a list, lower cases every word.

    currencyStr = ""
    for inpKW in inputKWs:
        if inpKW in currenciesList:
            currencyStr = inpKW
            break
        else:
            currencyStr = ""

    if currencyStr != "":
        return getDictKey(currencyCodesDict, currencyStr)  # Returns the currency code
    elif n < 3:
        print("Sorry, I can't recognise that currency. Maybe you've misspelled it?")
        return getFromCurrency(n + 1)
    else:
        return "noCurrency"


def getToCurrency(n):
    """Function takes as input:
        1. Int number 0 (for technical purposes)
        Function outputs:
        1. A the currency code, eg. "EUR", the user wants to convert from
        """

    print("Which currency do you wish to convert to?")
    inputKWs = lowercaseList1D(stringToKeywords(
        getUserInput()))  # Gets input string from user, stores all words in a list, lower cases every word.

    currencyStr = ""
    for inpKW in inputKWs:
        if inpKW in currenciesList:
            currencyStr = inpKW
            break
        else:
            currencyStr = ""

    if currencyStr != "":
        return getDictKey(currencyCodesDict, currencyStr)  # Returns the currency code
    elif n < 3:
        print("Sorry, I can't recognise that currency. Maybe you've misspelled it?")
        return getFromCurrency(n + 1)
    else:
        return "noCurrency"



ccStartupKWList = ["dollar", "krona", "peso", "krone", "forint", "koruna", "pound", "leu", "krona",
                   "rupiah", "rupee", "real", "ruble", "kuna", "yen", "baht", "franc", "euro", "ringgit", "lev",
                   "lira", "yuan", "rand", "shekel", "won", "zloty", "dollars", "kronas", "pesos", "krones", "forints", "korunas", "pounds", "leus", "kronas",
                   "rupiahs", "rupees", "reals", "rubles", "kunas", "yens", "bahts", "francs", "euros", "ringgits", "levs",
                   "liras", "yuans", "rands", "shekels", "wons", "zlotys", "money", "currency", "many", "is", "are", "convert", "to"]
keywordsList.append(ccStartupKWList)
def ccStartup():
    """This function initiates the currency converter"""
    contOrNot = input("I'll now help you convert currencies. Shall I continue?")

    if denial(contOrNot):
        print("Ok then, lets move on to something else.")
        return None

    fromCurrency = getFromCurrency(0)
    print("What is the amount you wish to convert?")
    amount = getUserInput()
    print("And which currency do you wish to convert to?")



def inputFilter(inputKWs):
    """This functions gets relevant data from the userInput
    Function input should be a list with the input broken into keywords."""



def currentConversion(amount, fromCurrency, toCurrency):
    """This function is used to convert currencies for current rates.
    The inputs consist of the currency to be converted from, to, and the amount.
    The function then outputs the conversion in a structured sentence with the following format:
    'At the moment, <amountBeforeConversion> <fromCurrency> is <valueAfterConversion> <toCurrency>'"""


def historicalConversion(amount, fromCurrency, toCurrency, fromDate, toDate):
    """This function is used to convert currencies for historical rates.
    The inputs consist of the currency to be converted from, to, from when to when, and the amount.
    (the dates should come in a list of 3 elements, counting from index 0, the format should be:
    <from>or<to>Date[0] = YYYY; <from>or<to>Date[1] = MM; <from>or<to>Date[2] = DD (values should be integers).
    The function then outputs the conversion in a structured sentence with the following format:
    'On <date>, <amountBeforeConversion> <fromCurrency> was <valueAfterConversion> <toCurrency>'"""

print(getFromCurrency(0))






