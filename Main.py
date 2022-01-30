# bot.py
#test2
import random
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='^')

GUILD = os.getenv('DISCORD_GUILD')
@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord')
@bot.command(name='ip')
async def ip(ctx,a : discord.Member):
        random.seed(ctx.message.author.id)
        response = f'{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}'
        await ctx.send(response + a.id)

bot.run(TOKEN)