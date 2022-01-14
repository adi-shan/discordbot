import discord
from discord.ext import commands
import random
from urllib.parse import quote
invis = 0x2F3136


class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Events
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Bot is online.')


    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')
    
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = ['It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.', 
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't count on it.",
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(aliases=['purge'])
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
    
    @commands.command(aliases=['echo'])
    async def say(self, ctx, *, words):
        await ctx.send(words)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
  
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    async def search(self, ctx, *, content: commands.clean_content):

        number = 1
        if "," in content:
            stuff = content.split(",")
            content = ",".join(stuff[:-1])
            number = max(
                min(int(stuff[-1].strip()) if stuff[-1].strip().isdigit() else 1, 10), 1
            )

    
        links = await self.bot.requests.get_json(f"https://gurgle.nathaniel-fernandes.workers.dev/?q={quote(content)}")
        if links is None or len(links) == 0:
            return await ctx.embed(title= 'No results found.')


        if len(links) == 0:
            return await ctx.embed(title="No Results Found!", color=invis)

        i = 0
        sent = False
        for link in links:
            if i == number:
                break

            # if await self.client.ahttp.is_media(link): THIS IS FOR MORE STRICT
            i += 1
            sent = True
            await ctx.embed(
                image_url=link, footer={"text": f"search term: {content}"}, color=invis
            )

        if not sent:
            return await ctx.embed(title="No Results Found!", color=invis)

    
def setup(bot):
    bot.add_cog(Basic(bot))
