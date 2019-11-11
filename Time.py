# Importing from the time module
from time import time,ctime

#KW=["time","date","month","today","day"]
def GetTime():
    # Return current time string
    return ctime(time())
