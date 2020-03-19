import os

import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

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
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the X-TREME dabber squad \o7! Don\'t forget to dab with caution haha!!'
    )
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dab_quotes = [
        'Hey guys, don\'t forget to dab with caution in these trying times! \o7',
        'Whoa \o7 almost missed that crucial dab. Keep it up fellow dabbers!',
    ]

    if message.content == '!dabtip':
        response = random.choice(dab_quotes)
        await message.channel.send(response)
    elif message.content == '!alan':
        response = 'Soooooo.... ummmm.... to reiterate.....'
        await message.channel.send(response)

client.run(TOKEN)