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
async def sendmessage(ctx,channel:discord.TextChannel, *text):
    await channel.send(' '.join(text))

@bot.event
async def on_message(message):
    channel = bot.get_channel('458778457539870742')
    if message.server is None and message.author != bot.user:
        await bot.send_message(channel, message.content)
    await bot.process_commands(message)

# This always sends the same message to the same person.  Is that what you want?
@bot.command(pass_context=True)
@commands.is_owner()  # The account that owns the bot
async def dm(ctx):
    memberID = "ID OF RECIPIENT"
    person = await bot.get_user_info(memberID)
    await bot.send_message(person, "WHAT I'D LIKE TO SAY TO THEM")
    await bot.delete_message(ctx.message)



bot.run(TOKEN)

