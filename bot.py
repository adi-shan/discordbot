import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv


from modules import AIOHTTP

load_dotenv()

bot = commands.Bot(command_prefix = '!')

bot.requests = AIOHTTP(timeout=5)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(f'{extension} has loaded.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(f'{extension} has been unloaded.')

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f'{extension} has reloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
# @bot.command()
# async def search(ctx, *, search_term, ammount=5):
#         print(f"https://gurgle.nathaniel-fernandes.workers.dev/?q={qoute(search_term)}")

@bot.event
async def on_ready():
    print('Bot is now active')

@bot.event 
async def on_message(message):
    if message.author == bot.user:
        return
    user = message.author
    msg = message.content
    print(f"{user} said {msg}")

    await bot.process_commands(message)

# @bot.event
# async def on_message_delete(message):
#     await message.channel.send("There was a message deleted here")
    

# @bot.command()
# async def ping(ctx):
#     await ctx.send('Pong!')

# @bot.command(aliases =['8ball'])
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

# @bot.command()
# async def clear(ctx, amount=5):
#     await ctx.channel.purge(limit=amount)

# @bot.command(aliases=['echo'])
# async def say(ctx, *, words):
#     await ctx.send(words)

# @bot.command()
# async def kick(ctx, member : discord.Member, *, reason=None):
#     await member.kick(reason=reason)

# @bot.command()
# async def ban(ctx, member : discord.Member, *, reason=None):
#     await member.ban(reason=reason)

# @bot.command()
# async def unban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_discriminator = member.split('#')

#     for ban_entry in banned_users:
#         user = ban_entry.user

#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f'Unbanned {user.mention}')
#             return

bot.run(os.environ.get('TOKEN'))

