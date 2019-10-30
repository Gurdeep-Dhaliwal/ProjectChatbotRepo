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
    
