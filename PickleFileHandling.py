import pickle,os.path

def FileCheck(FileName):
    # Function to check if the file already exists with the specified FileName argument.
    # If the file does not already exist, it will return False, else it will return True.
    if os.path.isfile(FileName)==False:
        return False
    else:
        return True

def FileRead(FileName):
    # Function to read a file with the specified FileName argument.
    # Begins using the FileCheck function, if this returns True, it will run the rest of the function and read the file.
    # If FileCheck returns anything else, e.g. False, this function will then return a string informing the user the file does not exist.
    if FileCheck(FileName)==True:
        FileRead=open(FileName,"rb")
        Data=pickle.load(FileRead)
        FileRead.close()
        return Data
    else:
        return "File does not exist."

def FileWrite(FileName,Data):
    # Function to write the data given by the Data argument to a file with the file name given by FileName.
    FileWrite=open(FileName,"wb")
    pickle.dump(Data,FileWrite)
    FileWrite.close()
