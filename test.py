from main import *


# Test functionRun()
greetingsGeneral()
while True:

    functionRun()


"""
while True:

    def triggerIt():
        @client.event
        async def on_message(message):
            globalInput = message
            functionRun()
"""

# Test goodbye()
#userDetailsList.append("")
#goodbye()


#import json
#from urllib.request import urlopen
from data import *
from generalFunctions import *
#from data import *

# The link in the code below was copied from an API's website.
# The links imported throughout this module can be found on the website below
# Link to API website: https://exchangeratesapi.io/
#with urlopen("https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01&base=USD") as urlContent:
#   src = urlContent.read()
# end of copied code

# jsonContentObj = json.loads(src)
# jsonContentStr = json.dumps(jsonContentObj["rates"]["2018-05-04"], indent=4)  # the dictionary was converted to a list for readability.
# print(jsonContentStr)
# print(jsonContentObj["rates"]["CAD"])  # Example of how to retrieve data

#ccStartupKWList = [""]
#keywordsList.append(ccStartupKWList)
#def ccStartup(inputKWs):
"""This function initiates the currency converter"""
"""
with urlopen("https://api.exchangeratesapi.io/latest") as content:
    src = content.read()

jsObject = json.loads(src)
jsStr = json.dumps(jsObject, indent=4)
print(jsStr)
"""

# print(getDictKey(currencyCodesDict, "pound"))
