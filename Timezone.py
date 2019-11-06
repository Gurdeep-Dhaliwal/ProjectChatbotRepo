from time import time,ctime
from datetime import datetime

def GetUTCTime():
    TimeArray=[]
    UTCTime=str(datetime.utcnow())
    UTCString=""
    TimeString=ctime(time())

    TimeArray.append(TimeString[0:3])
    TimeArray.append(TimeString[4:7])
    if TimeString[8]==" ":
        TimeArray.append(TimeString[9:10])
    else:
        TimeArray.append(TimeString[8:10])
    TimeArray.append(UTCTime[11:13])
    TimeArray.append(TimeString[14:16])
    TimeArray.append(TimeString[17:19])
    TimeArray.append(TimeString[20:25])
    for x in range(0,3):
        UTCString+=TimeArray[x]+" "
    for x in range(3,5):
        UTCString+=TimeArray[x]+":"
    UTCString+=TimeArray[5]+" "+TimeArray[6]
    return UTCString
