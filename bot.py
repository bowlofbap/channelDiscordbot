import os

import discord
import datetime

TOKEN = "NzI1NzE2NjQwMjU1MzExOTYz.XvSzmg.rNX4QMpGKZPJ6R4aUj-OXHHpv20"
GUILD = "pno/sw waiting room"

client = discord.Client()

users = {}

@client.event
async def on_ready():
    print(client.guilds)
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
    response = ""
    if '!rates' in message.content:
        message_info = message.content.split()
        amount = float(message_info[1])
        if message.author in users:
            user_info = users.pop(message.author)
            minutes = (datetime.datetime.now() - user_info["time"]).total_seconds() / 60
            total_gained = (amount - user_info["amount"]) 
            time = (datetime.datetime.now() - user_info["time"]).total_seconds() / 60 / 60
            rate = (amount - user_info["amount"]) / time
            response = message.author.name + " gained " + str(round(total_gained, 2)) + " in " + str(round(minutes, 2)) + " minutes. Rate is about " + str(round(rate, 2)) + " per hour"
        else:
            users[message.author] = {
                "time": datetime.datetime.now(),
                "amount": amount
            }
            response = "Starting timer for " + message.author.name
        await message.channel.send(response)

client.run(TOKEN)