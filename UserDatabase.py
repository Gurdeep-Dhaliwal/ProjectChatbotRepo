import sqlite3

"""The 'User' and 'NewUserData' argument for all functions should follow this format - [Name,Age,Gender,Nickname] and all fields must be in string format"""

def ConnectDatabase():
    # Function to connect to the database file ChatBotUsers.
    # It will attempt to create the required tables and pass if there is an error,
    # the result of this means that if there is no file with the tables, it will all be created automatically.
    with sqlite3.connect("ChatBotUsers.db") as db:
        cr=db.cursor()
    try:
        cr.execute("""CREATE TABLE Users(
        User_ID varchar(100),
        Name varchar(20),
        Age varchar(3),
        Gender varchar(10),
        Nickname varchat(30)
        );""")
        db.commit()
    except:
        pass
    return cr,db

def Hash(Text):
    # Function to generate a unique ID value for a new user based upon their personal data
    HashValue=""
    for CurrentPosition in range (len(Text)):
        HashValue+=str(ord(Text[CurrentPosition]))
    return HashValue

"""If using the SecureString function outside of the database script, the Type argument MUST either be "E" for Encryption or "D" for Decryption"""
def SecureString(String,Type):
    # Function to encrypt or decrypt, (specified using the Type argument as either "E" or "D"), a string using a Caesar Cipher method,
    # subtracting or adding to a character's ASCII value dependant on their position in the string and the length of the string overall.
    # Once encrypted or decrypted, it will return the new secure string.
    NewString=""
    for CharacterCount in range(len(String)):
        CharacterChanging=String[CharacterCount]
        OriginalAsci=ord(CharacterChanging)
        if Type=="E":
            NewAsci=OriginalAsci+CharacterCount+len(String)
            if NewAsci>255:
                NewAsci-=255
        if Type=="D":
            NewAsci=OriginalAsci-(CharacterCount+len(String))
            if NewAsci<0:
                NewAsci+=255
        NewCharacter=chr(NewAsci)
        NewString+=NewCharacter
    return NewString

def InputUser(User):
    # Function will take an array and try to put it into the ChatBotUsers database within the Users table.
    # The data is encrypted first using the SecureString function.
    # If there is an error, the function will return a string informing the user of this, else it will return a string informing them the action was successful.
    cr,db=ConnectDatabase()
    User_ID=Hash(User[0]+User[1]+User[2]+User[3])
    if 1==1:
        cr.execute("""INSERT INTO Users (User_ID,Name,Age,Gender,Nickname)
        VALUES(?,?,?,?,?)""",(User_ID,SecureString(User[0],"E"),SecureString(User[1],"E"),SecureString(User[2],"E"),SecureString(User[3],"E")))
        db.commit()
        return "Success"
    else:
        return "Error adding user to database."

def SearchForUser(User):
    # Function will take a search input under the argument User_ID_Search.
    # The function will attempt to find the record in the database with the given User_ID.
    # If a record is found, it will return the record as an array of the individual field values.
    # If a record is not found, it will return a string informing the user of this.
    cr,db=ConnectDatabase()
    try:
        HashValue=Hash(User[0]+User[1]+User[2]+User[3])
        cr.execute("""SELECT * FROM Users WHERE User_ID=?""",(HashValue,))
        User=[HashValue]
        for ArrayPos in cr.fetchall():
            for UserPos in range(1,5):
                User.append(SecureString(ArrayPos[UserPos],"D"))
        return User
    except:
        return "User not found."

def GetUser():
    # Function to get the user record from the database and return it
    cr,db=ConnectDatabase()
    cr.execute("SELECT * FROM Users")
    User=[]
    for x in cr.fetchall():
        for y in x:
            User.append(SecureString(y,"D"))
    return User[1:]

"""If a field does not need to be updated, input a blank string for its position in the User array, e.g. [User_ID,"","19",""] to only update a user's age"""
def UpdateUser(User,NewUserData):
    # Function to update a record in the databse where the given data under the User argument is the current record,
    # and the data under the NewUserData argument is the new data to be put into the database into the old record.
    # Function will attempt to update the record with the data, if an error is encountered, it will return a string informing the user of this,
    # else it will return a string informing them the action was successful.
    cr,db=ConnectDatabase()
    try:
        for x in range(len(NewUserData)):
            if NewUserData[x]=="":
                NewUserData[x]=User[x]
        OldHashValue=Hash(User[0]+User[1]+User[2]+User[3])
        NewHashValue=Hash(NewUserData[0]+NewUserData[1]+NewUserData[2]+NewUserData[3])
        cr.execute("""UPDATE Users SET User_ID=?,Name=?,Age=?,Gender=?,Nickname=? WHERE User_ID=?""",(NewHashValue,SecureString(NewUserData[0],"E"),SecureString(NewUserData[1],"E"),SecureString(NewUserData[2],"E"),SecureString(NewUserData[3],"E"),OldHashValue))
        db.commit()
        return "Success."
    except:
        return "Error updating user in database."

"""Only use this function for testing purposes to see all data within the database"""
def ShowData():
    # Function to aid in testing the of using the database,
    # the function will print all of the data in the database.
    cr,db=ConnectDatabase()
    cr.execute("SELECT * FROM Users")
    for x in cr.fetchall():
        print()
        print(x)
        print(x[0]+", "+SecureString(x[1],"D")+", "+SecureString(x[2],"D")+", "+SecureString(x[3],"D")+", "+SecureString(x[4],"D"))
