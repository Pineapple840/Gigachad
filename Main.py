# bot.py
#test2
import datetime
import random
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='^',help_command = None)
client = discord.Client
GUILD = os.getenv('DISCORD_GUILD')

@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord')

@bot.command()
async def ip(ctx,member : discord.Member = None):
    if member is None:
        member = ctx.message.author

    random.seed(member.id)
    response = f'{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}'
    await ctx.send(response)

@bot.command()
async def help(ctx):
    await ctx.send("""
    **ip** - Get a user's ip adress
    """)

@bot.command()
async def message(ctx,channel : discord.Channel, text):
    

bot.run(TOKEN)

