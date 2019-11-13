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
    """Function requests the currency the user wishes to convert from and outputs the corresponding currency code."""
    # IMPORTANT: Function should be started with argument 0.

    print("Which currency do you wish to convert from?")
    inputKWs = lowercaseList1D(stringToKeywords(getUserInput()))  # Gets input string from user, stores all words in a list, lower cases every word.

    fromCurrencyStr = ""
    for i in inputKWs:
        if i in currenciesList:
            fromCurrencyStr = i
        else:
            if n < 3:
                print("Sorry, I can't recognise that currency.")
                inputKWs.clear()
                getFromCurrency(n + 1)
            else:
                return "noCurrency"

    currencyCode = getDictKey(currencyCodesDict, fromCurrencyStr)
    return currencyCode




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

    print("Which currency do you wish to convert from?")
    fromCurrency = getUserInput()
    print("What is the amount you wish to convert?")
    amount = getUserInput()
    print("And which currency do you wish to convert?")



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






