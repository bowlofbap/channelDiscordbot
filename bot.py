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
        'When you are thinking its a good time to dab... don\'t.',
        'There’s only one type of dab that’s cool, and it ain’t \o7',
    ]
    alan_quotes = [
        'Soooooo.... ummmm.... to reiterate.....',
        'What is your onboarding process like?',
        'Ummmm, I have a follow up...',
        'With the current political landscape......',
        'Has someone ever answered the question with just, \'yes\'?',
        'So I think this is something that you\'ve already answered in the past but...',
        'Hey everyone, I know no one cares but I feel like I killed those interviews!',
        'For me at least... Umm...',
    ]
    frank_quotes = [
        '*Drinks diet mountain dew*',
        'You killed two stones with one bird.',
        'You okay Vinny?',
        'Jake\'s giving me that face again...',
        'Kyle - I mean Dan',
        'I think Chris is a serial killer.',
        'That\'s something that Jason would do.',
        'This is America, you can do what you want.',
        'Son of a Ginzo..',
        'I know you hate that Jake.',
        '*Stares at you like you\'re a dumbass*',
        'Aww man, what a knucklehead!',
        'Let\'s go over to our good buddy...',
        'C\'mon keyboard, stop messin\' me up.',
        'I watched that dabbing video.  Seems kinda dumb.',
        'It\'s a bad day when you can\'t spell \'fat arrow\'.',
        'Bear with me here for a Ginzo second.',
        'Stay tuned!',
        'What is the question ACTUALLY asking you?',
        'What\'re you doing knucklehead?',
        'Shanygne, did I spell your name right?',
        'Ah, I got a pain in my arm.',
        'Holy mackerel!',
        'Jason, if you do this I\'m flunking you.',
        'Oh crap...!',
        'Phew, close one.',
    ]

    if '!dabtip' in message.content:
        response = random.choice(dab_quotes)
        await message.channel.send(response)
    elif '!alan' in message.content:
        response = random.choice(alan_quotes)
        await message.channel.send(response)
    elif '!frank' in message.content:
        response = random.choice(frank_quotes)
        await message.channel.send(response)
    elif '!dew' in message.content:
        t_file = open("dewcounter", "r")
        dew_counter = int(t_file.read()) + 1
        t_file = open("dewcounter", "w")
        t_file.write(str(dew_counter))
        t_file.close()
        response = "Total Mountain Dew count: " + str(dew_counter)
        await message.channel.send(response)

client.run(TOKEN)