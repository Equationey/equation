import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('OTAzMzIzODE3NjEzNjExMDU5.YXrT3Q.9_WWuEq9ZhOOPE0gxjywJItOn2w')