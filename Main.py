from datetime import date
import random
import os

import discord
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))

intents=discord.Intents.all()
client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix='^',help_command = None, intents = intents)
tree = app_commands.CommandTree(client)



@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD))
    print('Gigachad is connected to Discord')
    #channel = bot.get_channel(939611555815891006)
    #await channel.send('hi')

@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=GUILD))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_message(message):
    if 'uwu' in message.content or 'owo' in message.content:
        await message.channel.send('https://tenor.com/view/stop-it-get-some-help-gif-15058124')
    if message.content == '^speechbubble':
        await message.delete()
    await bot.process_commands(message)

@bot.command()
async def russianroulette(ctx):
    random.seed()
    russianroulettechance = random.randrange(0,6)
    finnscheatcode = ctx.message.author.id
    if finnscheatcode == 717732515292643338 or russianroulettechance != 3:
        await ctx.send("You survive :grin:")
    else:
        await ctx.send("You die :skull:")

@bot.command()
async def speechbubble(ctx):
    message = ctx.message.id
    random.seed()
    SpeechOutput = ['https://tenor.com/view/lil-nas-x-nickb-pregnant-speech-bubble-gif-25238772', \
    'https://tenor.com/view/nerd-nerd-alert-meme-speech-bubble-glasses-gif-25033886',\
    'https://tenor.com/view/felix-re-zero-felix-argyle-speech-bubble-speech-gif-25397116',\
    'https://tenor.com/view/bubble-text-owl-text-bubble-bubble-text-owl-bubble-text-speech-bubble-owl-gif-25466686',\
    'https://tenor.com/view/speech-bubble-discord-who-cares-handsome-squidward-squidward-gif-25418980',\
    'https://tenor.com/view/furry-speech-bubble-gif-25272617',\
    'https://tenor.com/view/discord-japanese-goblin-speech-bubble-gif-25424326',\
    'https://tenor.com/view/cat-kitten-speech-bubble-speech-discord-gif-25192162'\
    'https://tenor.com/view/squidders-squid-reaction-speech-bubble-squid-speech-bubble-gif-25693400',\
    'https://tenor.com/view/cat-kitten-spilling-milk-milk-spilling-gif-25553835'\
    'https://tenor.com/view/sploot-speech-bubble-gif-25277146'\
    'https://tenor.com/view/women-moment-bubble-speech-women-talking-women-moment-women-speech-bubble-women-moment-women-talking-gif-25175116',\
    'https://tenor.com/view/smadging-speech-bubble-speech-bubble-smadging-gif-26061412',\
    'https://tenor.com/view/cat-typing-speech-bubble-kitty-gif-25862715',\
    'https://tenor.com/view/speech-bubble-cat-gif-25478740',\
    'https://tenor.com/view/speech-bubble-discord-lucky-star-konata-izumi-lazy-gif-25766360',]

    await ctx.send(random.choice(SpeechOutput))


@bot.command()
async def deathdate(ctx,member : discord.Member = None):

    if member is None:
        member = ctx.message.author

    random.seed(member.id)
    year = date.today().year + 1

    await ctx.send(f'{member} will die on {random.randrange(1,29)}/{random.randrange(1,13)}/{random.randrange(year,2100)}')

@tree.command(name = 'ip',description = "My first application Command", guild=discord.Object(id=GUILD))
async def ip(interaction: discord.Interaction, member : discord.Member = None):
    if member is None:
        member = interaction.user

    random.seed(member.id)
    response = f'{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}'
    await interaction.response.send_message(f'{response} is the IP address of {member}')

@bot.command()
async def token(ctx,member : discord.Member = None):
    if member is None:
        member = ctx.message.author

    response = ''
    random.seed(member.id)
    for i in range(56):
        letter = random.choice('1234567890._QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
        response += letter
    await ctx.send(f'{response} is the Discord token of {member}')


print("Gigachad is connecting to Discord...")
client.run(TOKEN)