import os
#import discord
import random
from discord.ext import commands
import requests
#from dotenv import load_dotenv

#load_dotenv()

TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')

# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

print(f"yahan pe --> ", TOKEN)

#client = discord.Client()

bot = commands.Bot(command_prefix='!')

def get_covid_stat():
    url = "https://api.covid19api.com/summary"
    
    dictCov = {}
    list1 = []
    
    try:
        req = requests.get(url)
        print("Status Code: ",  req.status_code)
        res_dict = req.json()
        list1 = res_dict['Countries']
    
        for items in range(0, len(list1) - 1):
            dictCov = list1[items]
            if dictCov['Country'] == "India":
                break
            dictCov = {}
    except ValueError:
        print('Decoding JSON has failed. Problem with API Call')
    
    # listCov.append(dictCov['TotalConfirmed'])
    # listCov.append(dictCov['TotalRecovered'])
    # listCov.append(dictCov['TotalDeaths'])
    
    return dictCov

@bot.command(name='covid', help="This command shows India's Covid Statistics")
async def covid(ctx):
    await ctx.send(get_covid_stat())

@bot.command(name='gn', help="This command greets good night")
async def gn(ctx):
    userName = str(ctx.message.author)
    formattedName, _ = userName.split("#")
    response = "Sleep tight, " + formattedName + " :)"
    await ctx.send(response)

@bot.command(name='gm', help="This command greets good morning")
async def gm(ctx):
    userName = str(ctx.message.author)
    formattedName, _ = userName.split("#")
    response = "A very goooood morning... " + formattedName + " :)"
    await ctx.send(response)

@bot.command(name='hello', help="This command greets hello")
async def hello(ctx):
    userName = str(ctx.message.author)
    formattedName, _ = userName.split("#")
    response = "Hello, you dirty fellow " + formattedName + "! How are you?"
    await ctx.send(response)

@bot.command(name='hi', help="This command greets hello")
async def hi(ctx):
    userName = str(ctx.message.author)
    formattedName, _ = userName.split("#")
    response = "Hello, you dirty fellow " + formattedName + ". Hope you are doing awesome!"
    await ctx.send(response)

@bot.command(name='birth', help="This command checks whether anyone has birthday today!")
async def birthday_check(ctx):
    userName = str(ctx.message.author)
    formattedName, _ = userName.split("#")
    response = "No one has a Birthday today, " + formattedName + " !"
    await ctx.send(response)

@bot.command(name='dice', help="This command rolls a dice and shows a number between '1-6'")
async def rollDice(ctx):
    number = random.randint(1, 6)
    await ctx.send(number)

@bot.command(name='add', help="This command adds two numbers. Provide '!add' followed by 2 numbers with space")
async def add(ctx, firstNum: int, secondNum: int):
    number = firstNum + secondNum
    await ctx.send(number)

@bot.command(name='sub', help="This command subtracts two numbers. Provide '!sub' followed by 2 numbers with space")
async def sub(ctx, firstNum: int, secondNum: int):
    number = firstNum - secondNum
    await ctx.send(number)

@bot.command(name='mul', help="This command multiplies two numbers. Provide '!mul' followed by 2 numbers with space")
async def mul(ctx, firstNum: int, secondNum: int):
    number = firstNum * secondNum
    await ctx.send(number)

@bot.command(name='div', help="This command divices one num from another. Provide '!div' followed by 2 numbers with space")
async def div(ctx, firstNum: int, secondNum: int):
    number = firstNum / secondNum
    await ctx.send(float(number))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send('No such command, try "!help" for more info ...')


bot.run(TOKEN)
