from datetime import datetime

"""Call this subroutine at the start of the script, e.g. StartTime=GetCurrentTime()"""
def GetCurrentTime():
    # Function to return the current UTC time.
    return str(datetime.utcnow())[-12:]

"""Call this subroutine at the end of the script, e.g. CalculateTime(StartTime)"""
def CalculateTime(StartTime):
    # Function to calculate and return the difference between the current time and the start time as given by the argument StartTime, in seconds.
    # The argument should be retrieved using the GetCurrentTime function at the start of a program and later passed when the program finishes.
    FinishTime=GetCurrentTime()
    Seconds=float(FinishTime[-9:])-float(StartTime[-9:])
    Minutes=float(FinishTime[:2])-float(StartTime[:2])
    Seconds+=(Minutes*60)
    return Seconds
    
