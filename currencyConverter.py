from generalFunctions import *
from data import *
import datetime

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
        return str(getDictKey(currencyCodesDict, currencyStr))  # Returns the currency code
    elif n < 3:
        print("Sorry, I can't recognise that currency. Maybe you've misspelled it?")
        return getFromCurrency(n + 1)
    else:
        print("My patience isn't infinite. Please let's just move on. Try this later.")
        return "noCurrency"


def getToCurrency(n):
    """Function takes as input:
        1. Int number 0 (for technical purposes)
        Function outputs:
        1. A the currency code, eg. "GBP", the user wants to convert to
        """

    print("Which currency do you wish to convert to?")
    inputKWs = lowercaseList1D(stringToKeywords(getUserInput()))  # Gets input string from user, stores all words in a list, lower cases every word.

    currencyStr = ""
    for inpKW in inputKWs:
        if inpKW in currenciesList:
            currencyStr = inpKW
            break
        else:
            currencyStr = ""

    if currencyStr != "":
        return str(getDictKey(currencyCodesDict, currencyStr))  # Returns the currency code
    elif n < 3:
        print("Sorry, I can't recognise that currency. Maybe you've misspelled it?")
        return getFromCurrency(n + 1)
    else:
        print("My patience isn't infinite. Please let's just move on. Try this later.")
        return "noCurrency"


def getAmount(n):
    """Gets the amount the user wants to convert, checks if it's a number, rounds it to a 2 decimal point float, returns it"""
    # IMPORTANT: Function has to be started with input "0" as integer for technical purposes.

    print("What is the amount you wish to convert?")
    amount = getUserInput()

    if checkInputNumber(amount):  # Returns true if amount is a number. False otherwise.
        return round(float(amount), 2)
    elif n < 3:
        print('Please express the amount with numeric characters. Use "." to write decimals.')
        return getAmount(n + 1)
    else:
        print("Scandalous. It is scandalous... Just take a cold shower and try this afterwards.")
        return "noAmount"



ccStartupKWList = ["dollar", "krona", "peso", "krone", "forint", "koruna", "pound", "leu", "krona",
                   "rupiah", "rupee", "real", "ruble", "kuna", "yen", "baht", "franc", "euro", "ringgit", "lev",
                   "lira", "yuan", "rand", "shekel", "won", "zloty", "dollars", "kronas", "pesos", "krones", "forints", "korunas", "pounds", "leus", "kronas",
                   "rupiahs", "rupees", "reals", "rubles", "kunas", "yens", "bahts", "francs", "euros", "ringgits", "levs",
                   "liras", "yuans", "rands", "shekels", "wons", "zlotys", "money", "currency", "many", "is", "are", "convert", "to"]
keywordsList.append(ccStartupKWList)
def ccStartup():
    """This function initiates the currency converter"""
    print("I'll now help you convert currencies. Is that ok?")
    contOrNot = getUserInput()

    if denial(contOrNot):
        print("Ok then, lets move on to something else.")
        return None

    fromCurrency = getFromCurrency(0)
    amount = getAmount(0)
    toCurrency = getToCurrency(0)
    date = getDate(0)

    if fromCurrency == "noCurrency" or toCurrency == "noCurrency" or amount == "noAmount" or getDate == "noDate":
        return ""

    if date == "now":
        currentConversion(amount, fromCurrency, toCurrency)
    elif date == "noDate":
        return ""
    else:
        previousConversion(amount, fromCurrency, toCurrency, date)



def getOlderDate(n):
    """Specifically requests the user a date. Checks its format.
    Returns date if format YYYY-MM-DD is met. Returns 'noDate' if user fails to input a date with a valid format too many times."""
    # IMPORTANT: Function has to be started with input "0" as integer for technical purposes.

    print('Please tell me the date from which the conversion rates should be.\nFormat should be "YYYY-MM-DD", including the dashes. No spaces.')
    inputDate = getUserInput()

    try:
        dateList = ["", "", ""]
        userDateSplit = inputDate.split("-")  # Stores year, month and days, on the specified order.

        for i in range(len(userDateSplit)):
            dateList[i] = userDateSplit[i]

        date = datetime.datetime(int(dateList[0]), int(dateList[1]), int(dateList[2]))
        return date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d")

    except ValueError:
        if n < 3:
            print("You've either misspelled or typed in a wrong date.")
            return getOlderDate(n + 1)
        else:
            print("I have emotions too. I don't feel good asking for the same thing over and over again :(\nLets just move on. Try it all again later if you wish to.")
            return ""


def getDate(n):
    """Aks user for which dates they want the conversion rates to be from. Outputs the date."""

    print("Should I convert using current rates or from other date?")
    inpList = lowercaseList1D(stringToKeywords(getUserInput()))
    nowKWs = ["today", "now", "current", "updated", "latest", "recent", "new", "fresh", "newer", "newest"]
    thenKWs = ["before", "previous", "older", "past", "old", "historical", "earlier", "preceding", "anterior", "then", "other", "older"]

    nowOrThen = mostMatchedList(inpList, nowKWs, thenKWs)

    if nowOrThen == nowKWs:
        return "now"
    elif nowOrThen == thenKWs:
        return getOlderDate(0)
    else:
        print("Couldn't really decide... please rephrase and/or reword.")
        return getDate(n + 1)



def currentConversion(amount, fromCurrency, toCurrency):
    """This function is used to convert currencies for current rates.
    The inputs consist of the currency to be converted from, to, and the amount.
    The function then outputs the conversion in a structured sentence with the following format:
    'At the moment, <amountBeforeConversion> <fromCurrency> is <valueAfterConversion> <toCurrency>'"""

    if fromCurrency == toCurrency:
        rate = 1
    else:
        if fromCurrency == "EUR":
            rate = getJSonFromUrl("https://api.exchangeratesapi.io/latest")["rates"][toCurrency]
        else:
            rate = getJSonFromUrl("https://api.exchangeratesapi.io/latest?base=" + fromCurrency)["rates"][toCurrency]

    amountConverted = round(amount * rate, 2)
    print(str(amount) + " " + currencyCodesDict[fromCurrency][-1] + " is " + str(amountConverted) + " " + currencyCodesDict[toCurrency][-1] + ".")


def previousConversion(amount, fromCurrency, toCurrency, date):
    """This function is used to convert currencies for historical rates.
    The inputs consist of the currency to be converted from, to, from when to when, and the amount.
    (the dates should come in a list of 3 elements, counting from index 0, the format should be:
    <from>or<to>Date[0] = YYYY; <from>or<to>Date[1] = MM; <from>or<to>Date[2] = DD (values should be integers).
    The function then outputs the conversion in a structured sentence with the following format:
    'On <date>, <amountBeforeConversion> <fromCurrency> was <valueAfterConversion> <toCurrency>'"""

    if fromCurrency == toCurrency:
        rate = 1
    else:
        if fromCurrency == "EUR":
            if getJSonFromUrl("https://api.exchangeratesapi.io/history?start_at=" + date + "&end_at=" + date)["rates"] is None:
                print("Sorry, no rates are available for that date")
                return ""
            rate = getJSonFromUrl("https://api.exchangeratesapi.io/history?start_at=" + date + "&end_at=" + date)["rates"][date][toCurrency]
        else:
            if getJSonFromUrl("https://api.exchangeratesapi.io/history?start_at=" + date + "&end_at=" + date)["rates"] is None:
                print("Sorry, no rates are available for that date")
                return ""
            rate = getJSonFromUrl("https://api.exchangeratesapi.io/history?start_at=" + date + "&end_at=" + date + "&base=" + fromCurrency)["rates"][date][toCurrency]

    amountConverted = round(amount * rate, 2)
    print("On " + date + ", " + str(amount) + " " + currencyCodesDict[fromCurrency][-1] + " was " + str(amountConverted) + " " +
          currencyCodesDict[toCurrency][-1] + ".")


