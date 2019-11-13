import discord
import youtube_dl
import random as r
from discord.ext import commands
from discord.utils import get
import os
from Translation import *

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Complete')
    print(client.user.name)
    print(client.user.id)


@client.command()
async def hello(ctx):
    name = str(ctx.author.name)
    nick = str(ctx.author.nick)
    await ctx.send(f'Hello {name}')
    await ctx.send(f'Hello {nick}')


@client.command()
async def joke(ctx):
    jokeList = ['I was wondering why the ball was getting bigger. Then it hit me','I have a few jokes about unemployed people, but none of them work',"When life gives you melons, you're dyslexic",'How do you make holy water? You boil the hell out of it','I lost my job at the bank on my very first day. A woman asked me to check her balance, so I pushed her over','Did you hear about the guy whose whole left side was cut off? He’s all right now','The man who survived pepper spray and mustard gas is now a seasoned veteran' ]
    await ctx.send(jokeList[r.randint(0, len(jokeList))])


##command takes two arguments from the user and translates the first typed word into the language specified
@client.command()
async def translate(ctx, text, lang):
    await ctx.send(TranslateText(text,lang))

@client.command()
async def clear(ctx, total = 2):
    await ctx.channel.purge(limit = total)


@client.command()
async def start(ctx, video:str):
    there = os.path.isfile('video.mp3')
    if there:
        os.remove('video.mp3')

    voice_channel = get(client.voice_clients,guild = ctx.guild)
    guild = ctx.message.author.voice.channel
    voice_channel = await guild.connect()
    opts = {
    'outtmpl': r'C:\Users\georg\Documents\DiscordBot/video.mp3',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([video])



    voice_channel.play(discord.FFmpegPCMAudio('video.mp3'))

@client.command()
async def remove(ctx):
        voice_channel = get(client.voice_clients, guild=ctx.guild)
        await voice_channel.disconnect()






client.run('NjM2MzE5MDc1MTY0ODgwOTE2.Xa96jg.eDhEWStjlF_FeNiqNM7Qg2-GOks')
