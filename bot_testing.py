import discord 
from discord.ext import commands 

TOKEN = 'ODk0OTM0ODY4NjU0NDMyMzY2.YVxPCw.QwdH14pTVzbC2UoVOdE8pHxOeio'

client = commands.Bot(command_prefix = '.') 
client.remove_command('help')

@client.event
async def on_ready():
  print("Bot is ready")

@client.command 
async def ping():
  await client.say("Pong!")

@client.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author

  embed = discord.Embed(
    colour = discord.Colour.orange()
  )

  embed.set_author(name = "Help")
  embed.add_field(name = ".ping", value = "Returns Pong", inline = False)

  await client.send_message(author, Embed=embed)

client.run(TOKEN)
