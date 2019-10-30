# The following code has been developed by Leo Rudczenko.
# Any exceptions to the rule above will be appropriately pointed out, along with references to the code's origin.
# In case of anyone else's contribution, such should be registered in comments before and after the contribution itself.
# If it is only one line, just write it next to the line.

import pickle

def FileCheck(FileName):
    if os.path.isfile(FileName)==False:
        File=open(FileName,"wb")
        pickle.dump([""],File)
        File.close()

def FileRead(FileName):
    FileRead=open(FileName,"rb")
    Data=pickle.load(FileRead)
    FileRead.close()
    return Data

def FileWrite(FileName,Data):
    FileWrite=open(FileName,"wb")
    pickle.dump(Data,FileWrite)
    FileWrite.close()
