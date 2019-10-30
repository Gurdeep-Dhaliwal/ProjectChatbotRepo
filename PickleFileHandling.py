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
