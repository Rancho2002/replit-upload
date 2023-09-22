# This example requires the 'message_content' intent.

import discord
import os

MY_SECRET = os.getenv("SECRET_KEY")

# class MyClient(discord.Client):

#   async def on_ready(self):
#     print(f'Logged on as {self.user}!')

#   async def on_message(self, message):
#     print(f'Message from {message.author}: {message.content}')

# intents = discord.Intents.default()
# intents.message_content = True

# client = MyClient(intents=intents)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def solveEq(eq: str):
  s = eval(eq)
  return s


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  s = message.content
  try:
    response = solveEq(s)
    await message.channel.send(response)
  except:
    await message.channel.send(
        "Write equation only, without any additional word")


client.run(MY_SECRET)
