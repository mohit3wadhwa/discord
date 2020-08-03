import os
#import discord
import random
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()

TOKEN = os.environ.get('DISCORD_TOKEN')
GUILD = os.environ.get('DISCORD_GUILD')

# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

print(f"yahan pe --> ", TOKEN)

client = discord.Client()

bot = commands.Bot(command_prefix='!')


@bot.command(name='birth', help="This command checks whether anyone has birthday today!")
async def birthday_check(ctx):
    #response = "Today's no one's Birthday"
    response = "Today is Simi's Birthday :ballon"
    await ctx.send(response)


@bot.command(name='roll_dice', help="This command rolls a dice and shows a number between '1-6'")
async def rollDice(ctx):
    number = random.randint(1, 6)
    await ctx.send(number)


@bot.event
async def on_command_error(ctx, error):
    await ctx.send('No such command!')



bot.run(TOKEN)

# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')
#     print(type(members))
# client.run(TOKEN)
