import pickle


def FileRead(FileName):
    FileRead=open(FileName,"rb")
    Data=pickle.load(FileRead)
    FileRead.close()
    return Data


def FileWrite(FileName,Data):
    FileWrite=open(FileName,"wb")
    pickle.dump(Data,FileWrite)
    FileWrite.close()


#KeyWordsList=FileRead("KeyWords")
#print(KeyWordsList)
#FileWrite("KeyWords",KeyWordsList)
