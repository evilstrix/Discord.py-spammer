import discord.py # imports discord.py ( discord bot py module )
from discord.ext import comamnds # imports commands from discord cause if u dont do that it ll say error

intents = discord.Intents.default()
intents.message_content = True

TOKEN = "" # defines a variable for the token

bot = comamnds.Bot(command_prefix"!", intents=intents") # defines intent

@bot.event # a bot event
async def onready():
    print("succesfully logged in the bot") # logs 'Succesfully logged in the bot'

@bot.command # defines a bot command
async def spam(): # spam function
    for _ in range(100): # You can choose how many times to send the specified message, or you can replace it by while True: and it ll send messages infinitely
        await.channel.send(f"Hello, i am a spammer") # sends the content

bot.run(TOKEN)
