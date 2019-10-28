from main import *

# Test functionRun()
#while True:
    #functionRun()


# keywordsListSelection(stringToKeywords(getUserInput()))

boop = FileRead("KeyWordsFile")
del boop[0][-1]
FileWrite("KeyWordsFile", boop)
print(FileRead("KeyWordsFile"))