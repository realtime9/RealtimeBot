import discord
from discord.ext import commands

TOKEN = 'ODk0OTM0ODY4NjU0NDMyMzY2.YVxPCw.QwdH14pTVzbC2UoVOdE8pHxOeio'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is Ready')

@client.event
async def on_message_delete(messsage):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message[channel, '{}: {}'.format(author, content)]
client.run(TOKEN)
