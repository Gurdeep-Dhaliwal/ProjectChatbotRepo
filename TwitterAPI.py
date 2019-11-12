from random import randint
import twitter

#KW=["joke","laugh","funny"]
def GetTwitterJoke():
    # Function to retrieve a Tweet from a Twitter account which regular posts jokes.
    # Function will retrieve the 10 most recent Tweets from the account's timeline.
    # Function will extract the text from the Tweets and append them to an array of the returned text.
    # The function will then return a random joke from the array, using the random module to select a random position in the array.
    AccessToken="3188258938-W47VMmUXnJWvkza4YoEEPbL5NkFi0A7C2icFXpt"
    AccessTokenSecret="JyAZxYlt7GqQhzTj0LtnrqpyCJ94wzB05pDuCN3UytfDu"
    ConsumerKey="8JfJNFTP1HyI9hYvgv9lEqsFU"
    ConsumerSecretKey="1ny3apY6AEdxInWxu9rFdvLC4KPaAz5dbKECoufPnZ7Nksxs8g"
    TwitterAPI=twitter.Api(consumer_key=ConsumerKey,consumer_secret=ConsumerSecretKey,
                    access_token_key=AccessToken,access_token_secret=AccessTokenSecret)
    NewLine="\\n"
    Timeline=str(TwitterAPI.GetUserTimeline(screen_name="Dadsaysjokes",count=50)).replace(NewLine," ")
    ExtractingText=True
    TextArray=[]
    Text=""
    for x in range(len(Timeline)):
        if Timeline[x-5:x+1]=="Text='":
            y=x+1
            while ExtractingText==True:
                if Timeline[y]=="'":
                    if "https://" not in Text:
                        while RemovingWhiteSpace==True:
                            Text=Text.replace("  "," ")
                            if "  " not in Text:
                                RemovingWhiteSpace=False
                        if NewLine[0] not in Text:
                            TextArray.append(Text)
                    ExtractingText=False
                else:
                    Text+=Timeline[y]
                    y+=1
        Text=""
        ExtractingText=True
        RemovingWhiteSpace=True
    Text=TextArray[randint(0,len(TextArray))]
    WordArray=Text.split()
    try:
        if WordArray[0][0].upper()==WordArray[0][0] and WordArray[1][0].upper()==WordArray[1][0]:
            Text=Text[len(WordArray[0])+1:]
    except:
        pass
    return Text

print(GetTwitterJoke())
            
                


