import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '!')
TOKEN = "OTI3NzY5OTcyNTc3NTU4NjE5.YdPDHg.ZEMZfr3a1-b6QbfVvrjl1Qja2Fw"


@client.event
async def on_ready():
    print('Bot is now active')

client.run('OTI3NzY5OTcyNTc3NTU4NjE5.YdPDHg.ZEMZfr3a1-b6QbfVvrjl1Qja2Fw')

