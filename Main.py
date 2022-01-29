# bot.py
#test
import random
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
GUILD = os.getenv('DISCORD_GUILD')
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '^ip':
        random.seed(client.user.id)
        response = f'{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}'
        await message.channel.send(response)
client.run(TOKEN)