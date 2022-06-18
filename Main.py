# bot.py
#test2
from datetime import date
import random
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='^',help_command = None, intents = intents)
client = discord.Client
GUILD = os.getenv('DISCORD_GUILD')



@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord')
    #channel = bot.get_channel(939611555815891006)
    #await channel.send('hi')


@bot.event
async def on_message(message):
    if 'uwu' in message.content or 'owo' in message.content:
        await message.channel.send('https://tenor.com/view/stop-it-get-some-help-gif-15058124')
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
async def deathdate(ctx,member : discord.Member = None):

    if member is None:
        member = ctx.message.author

    random.seed(member.id)
    year = date.today().year + 1

    await ctx.send(f'{member} will die on {random.randrange(1,29)}/{random.randrange(1,13)}/{random.randrange(year,2100)}')

@bot.command()
async def ip(ctx,member : discord.Member = None):
    if member is None:
        member = ctx.message.author

    random.seed(member.id)
    response = f'{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}'
    await ctx.send(f'{response} is the IP address of {member}')

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

@bot.command()
async def help(ctx):
    await ctx.send("""
    **ip** - Get a user's ip address
    **russianroulette** - It's easy; no one has ever lost more than once
    **deathdate** - There is nothing you can do to change it
    """)

@bot.command()
async def sendmessage(ctx,channel:discord.TextChannel, *text):
    await channel.send(' '.join(text))

@bot.command()
async def gaysex(ctx, member1 : discord.Member = None, member2 : discord.Member = None):
    if member1 is None:
        member1 = "Gigachad"
    else:
        member1 = member1.name
    if member2 is None:
        member2 = ctx.message.author.name
    else:
        member2 = member2.name

    output = ("Kai is watching TV on his bed, when his boyfriend Alex comes home from the store. The two share a passionate kiss. Kai smirks devilishly and gestures Alex to come closer. Alex aroused quickly stripes naked. Kai does the same. Kai bends over on his knees into position on the bed. Alex quickly shoves his rock hard cock inside of Kai's ass. Alex pounds Kai as hard as he can. Kai's sexy moans make Alex come inside him. After Alex takes his cock out of Kai's ass, Alex pins Kai to the bed and spreads his legs apart while lifting them up. Alex puts his cock slowly in Kai's hole. Alex starts pushing in and pulling out at a steady pace. Kai moans while panting. After a few minutes they both come from pleasure. Kai, eager to get back at Alex, gets on his knees and starts sucking Alex's cock. Alex begins to moan with every mouth stroke. Kai starts to deep throat Alex and fondle his balls. Alex comes uncontrollably into Kai's mouth. Kai swallows it all and kisses the tip of Alex's cock as a tease. After the intense sex, the two took showers together and cuddled each other to sleep.").replace("Kai",member1)
    output2 = (output).replace("Alex",member2)
    await ctx.send(output2)

@bot.command()
async def valorant(ctx):
    member = random.choice(ctx.channel.guild.members)
    await ctx.send(member.name)

print("Gigachad is connecting to Discord...")
bot.run(TOKEN)