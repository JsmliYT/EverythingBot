import discord
from replit import db as dbs
import os
import requests
import json
import hashlib
from keep_alive import keep_alive
import random
import re
from urllib.parse import quote
import aiohttp
import asyncio
import ujson
import requests

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_daily():
  response = requests.get("https://zenquotes.io/api/today")
  json_data = json.loads(response.text)
  daily = json_data[0]['q'] + " -" + json_data[0]['a']
  return(daily)

# Startup Information
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Looking for *help'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content.startswith

  send = message.channel.send

  if msg('*inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg('*dailyinspire'):
    daily = get_daily()
    await message.channel.send(daily)
  
  if msg('*help'):
    await send("*inspire, use this command to get a inspirational quote. *dailyinspire, use this command to get the quote of the day. *ping, Pong!. *invite, use this command to get a invite to the bot. *support, use this command to get our discord server. *upcoming, use this command to learn about whats coming soon (hopefully). *hello, use this command to say hello to the owner")

  if msg('*ping'):
    await message.channel.send('Pong!')

  if msg('*invite'):
    await message.channel.send('To invite the bot use this website. https://top.gg/bot/807535418966933524')

  if msg('*support'):
    await message.channel.send("go here to join our server. https://discord.gg/bdWbS5Kz7E")

  if msg('*dashboard'):
    await message.channel.send('we DO NOT currently have a dashboard.')

  if msg('*suggest'):
    await message.channel.send('We are currently working on this command, in the mean time please use *support and go to our Discord server')

  if msg('*slash'):
    await message.channel.send("We most likely wont be using slash commands anytime soon as it is hard to do.")
  
  if msg('*embed'):
    await message.channel.send("we are working on trying to create Embeds. This will come in the future.")

  if msg('prefix'):
    await send("The prefix for our Bot is *")

  if msg('*upcoming'):
    await send("We are trying to get ModMail.")

  if message.content.startswith('*hello'):
   channel = client.get_channel(880001901750538271)
   await channel.send('Someone said Hello to you <@554147162708246550>')

keep_alive()
client.run(os.getenv('TOKEN'))