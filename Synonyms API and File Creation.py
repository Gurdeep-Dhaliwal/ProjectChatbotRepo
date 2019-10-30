import requests
from PickleFileHandling import *
from Stopwatch import *

def GetWord(Word):
    Words=[]
    Parameter={"ml":Word}
    Request=requests.get("https://api.datamuse.com/words",Parameter)
    JsonData=Request.json()
    Words.append(Word)
    for i in JsonData[0:4]:
        Words.append(i["word"])
    return Words

def Create3DWordArray(WordList):
    WordArrays=[]
    for i in WordList:
        WordArrays.append(GetWord(i))
    return WordArrays

StartTime=GetCurrentTime()

FileWrite("KeyWordsFile",Create3DWordArray(["hello","weather","music","climate"]))
print(FileRead("KeyWordsFile"))

print(CalculateTime(StartTime))


