import sqlite3

"""The 'User' argument for all functions should follow this format - [Discord_ID,Name,Age,Gender] and all fields must be in string format"""

def ConnectDatabase():
    # Function to connect to the database file ChatBotUsers.
    # It will attempt to create the required tables and pass if there is an error,
    # the result of this means that if there is no file with the tables, it will all be created automatically.
    with sqlite3.connect("ChatBotUsers.db") as db:
        cr=db.cursor()
    try:
        cr.execute("""CREATE TABLE Users(
        Discord_ID varchar(20),
        Name varchar(20),
        Age varchar(3),
        Gender varchar(10)
        );""")
        db.commit()
    except:
        pass
    return cr,db

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
    cr=ConnectDatabase()
    try:
        cr.execute("""INSERT INTO Users (Discord_ID,Name,Age,Gender)
        VALUES(?,?,?,?)""",(SecureString(Discord_ID,"E"),SecureString(Name,"E"),SecureString(Age,"E"),SecureString(Gender,"E")))
        db.commit()
        return "Success"
    except:
        return "Error adding user to database."

def SearchForUser(Discord_ID_Search):
    # Function will take a search input under the argument Discord_ID_Search.
    # The function will attempt to find the record in the database with the given Discord_ID.
    # If a record is found, it will return the record as an array of the individual field values.
    # If a record is not found, it will return a string informing the user of this.
    cr,db=ConnectDatabase()
    try:
        cr.execute("""SELECT * FROM Users WHERE Discord_ID=?""",(SecureString(Discord_ID_Search,"E"),))
        User=[]
        for ArrayPos in cr.fetchall():
            for UserPos in range(4):
                User.append(SecureString(ArrayPos[UserPos],"D"))
        return User
    except:
        return "User not found."

"""If a field does not need to be updated, input a blank string for its position in the User array, e.g. [Discord_ID,"","19",""] to only update a user's age"""
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
        cr.execute("""UPDATE Users SET Name=?,Age=?,Gender=? WHERE Discord_ID=?""",(SecureString(NewUserData[1],"E"),SecureString(NewUserData[2],"E"),SecureString(NewUserData[3],"E"),SecureString(User[0],"E")))
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
        print(SecureString(x[0],"D")+", "+SecureString(x[1],"D")+", "+SecureString(x[2],"D")+", "+SecureString(x[3],"D"))
