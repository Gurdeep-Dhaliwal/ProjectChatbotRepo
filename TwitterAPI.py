from random import randint
import twitter,json

def GetTwitterJoke():
    AccessToken="3188258938-W47VMmUXnJWvkza4YoEEPbL5NkFi0A7C2icFXpt"
    AccessTokenSecret="JyAZxYlt7GqQhzTj0LtnrqpyCJ94wzB05pDuCN3UytfDu"
    ConsumerKey="8JfJNFTP1HyI9hYvgv9lEqsFU"
    ConsumerSecretKey="1ny3apY6AEdxInWxu9rFdvLC4KPaAz5dbKECoufPnZ7Nksxs8g"

    TwitterAPI=twitter.Api(consumer_key=ConsumerKey,consumer_secret=ConsumerSecretKey,
                    access_token_key=AccessToken,access_token_secret=AccessTokenSecret)

    Timeline=str(TwitterAPI.GetUserTimeline(screen_name="Dadsaysjokes",count=100)).replace("\\n"," ")
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
                                TextArray.append(Text)
                                RemovingWhiteSpace=False
                    ExtractingText=False
                else:
                    Text+=Timeline[y]
                    y+=1
        Text=""
        ExtractingText=True
        RemovingWhiteSpace=True
    return TextArray[randint(0,len(TextArray))]
            
                


