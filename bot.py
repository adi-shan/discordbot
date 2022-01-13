import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
TOKEN = "OTI3NzY5OTcyNTc3NTU4NjE5.YdPDHg.ZEMZfr3a1-b6QbfVvrjl1Qja2Fw"

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} has loaded.')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'{extension} has been unloaded.')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'{extension} has reloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print('Bot is now active')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    user = message.author
    msg = message.content
    print(f"{user} said {msg}")

    await client.process_commands(message)

# @client.event
# async def on_message_delete(message):
#     await message.channel.send("There was a message deleted here")
    

# @client.command()
# async def ping(ctx):
#     await ctx.send('Pong!')

# @client.command(aliases =['8ball'])
# async def _8ball(ctx, *, question):
#     responses = ['It is certain.',
#     'It is decidedly so.',
#     'Without a doubt.',
#     'Yes - definitely.',
#     'You may rely on it.', 
#     'As I see it, yes.',
#     'Most likely.',
#     'Outlook good.',
#     'Yes.',
#     'Signs point to yes.',
#     'Reply hazy, try again.',
#     'Ask again later.',
#     'Better not tell you now.',
#     'Cannot predict now.',
#     'Concentrate and ask again.',
#     "Don't count on it.",
#     'My reply is no.',
#     'My sources say no.',
#     'Outlook not so good.',
#     'Very doubtful.']
#     await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# @client.command()
# async def clear(ctx, amount=5):
#     await ctx.channel.purge(limit=amount)

# @client.command(aliases=['echo'])
# async def say(ctx, *, words):
#     await ctx.send(words)

# @client.command()
# async def kick(ctx, member : discord.Member, *, reason=None):
#     await member.kick(reason=reason)

# @client.command()
# async def ban(ctx, member : discord.Member, *, reason=None):
#     await member.ban(reason=reason)

# @client.command()
# async def unban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_discriminator = member.split('#')

#     for ban_entry in banned_users:
#         user = ban_entry.user

#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f'Unbanned {user.mention}')
#             return

client.run('OTI3NzY5OTcyNTc3NTU4NjE5.YdPDHg.ZEMZfr3a1-b6QbfVvrjl1Qja2Fw')

