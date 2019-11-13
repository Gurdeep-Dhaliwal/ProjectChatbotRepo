"""All validation functions will return 0 if the data passes the validation testing or 1 if it fails the validation testing"""

"""Data should be a single string and DataLen must be an integer"""
def CheckTextField(Data,DataLen):
    # Function to check if the given data under the Data argument is valid for the given valid length of data under the DataLen argument,
    # or if the string data is an empty string.
    # If the data passes the validation tests, the function will return 0, if not, the function will return 1.
    Data=Data.strip().lower().title()
    try:
        Pass=0        
        if Data=="" or len(Data)>DataLen:
            Pass=1
    except:
        Pass=1
    return Pass

"""Data should be a single integer and DataRange should be a list of 2 integers, the first being the lower end of the range, the second being the higher end of the range"""
def CheckIntegerField(Data,DataRange):
    # Function to check if the given data under the Data argument is valid for the given valid range of data under the DataRange argument.
    # If the data passes the validation tests, the function will return 0, if not, the function will return 1.
    Data=Data.strip()
    try:
        Pass=0
        if Data<DataRange[0] or Data>DataRange[1]:
            Pass=1
    except:
        Pass=1
    return Pass

"""DataList should be an array of the options which Data can be, the Data and values in DataList should be in the same format"""
def CheckOptionField(Data,DataList):
    # Function to check if the given data under the Data argument is in the given list under the argument DataList.
    # If the data passes the validation tests, the function will return 0, if not, the function will return 1.
    Data=Data.strip().lower().title()
    try:
        Pass=0
        if Data.lower() not in DataList:
            Pass=1
    except:
        Pass=1
    return Pass
