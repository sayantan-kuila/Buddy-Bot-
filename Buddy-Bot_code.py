import discord
#connection to the discord server 
import os

#request module helps to request to collect data from an API
import requests
import json
import random
#to import keep_alive and to make the bot awake
from keep_alive import keep_alive


client=discord.Client()

#sad_words are the key words used to trigger quotes and starter_encouragements helps to give random answers when sad_words are used

sad_words=["sad","disappointed","bad","unhappy","depressed","miserable","angry"]

starter_encouragements=[
  "Bro chill !",
  "We all are virgins! ",
  "Cheer up!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random") #you can choose your own api and add it here.
  json_data = json.loads(response.text)
  quote =  '**"' + json_data[0]['q'] + '"**' + "** -" + json_data[0]['a'] + '**' 
  return(quote)


@client.event
#on_ready function will trigger when it is launched in the server
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
#on_message will trigger when it receives a message from the user
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$help"):
    await message.channel.send("$inspire - for quote\n$hello - greetings")

  if msg.startswith("$hello"):
    await message.channel.send("Hi user!")


  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

#delivers a random message from starter_encouragements when sad_words are used
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

#calling the function
keep_alive()
client.run(os.getenv('TOKEN'))
