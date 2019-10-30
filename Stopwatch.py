# The following code has been developed by Leo Rudczenko.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# In case of anyone else's contribution, such should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

from datetime import datetime

# Call this subroutine at the start of the script, StartTime=GetCurrentTime()
def GetCurrentTime():
    return str(datetime.utcnow())[-12:]

# Call this subroutine at the end of the script, CalculateTime(StartTime)
def CalculateTime(StartTime):
    FinishTime=GetCurrentTime()
    Seconds=float(FinishTime[-9:])-float(StartTime[-9:])
    Minutes=float(FinishTime[:2])-float(StartTime[:2])
    Seconds+=(Minutes*60)
    return Seconds
    
