import discord
from discord.ext import commands
import random
from urllib.parse import quote
invis = 0x2F3136


class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def drake(self, ctx, *, content: commands.clean_content):
        stuff = content.split(',')
        first = stuff[0]
        second = stuff[1].strip() if len(stuff) == 2 else ''
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/drake?nah={quote(first)}&yeah={quote(second)}")

    @commands.command()
    async def metaverse(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/metaverse?text={quote(content)}")
    
    @commands.command()
    async def achievement(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/achievement?text={quote(content)}")

    @commands.command()
    async def cantread(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/cantread?text={quote(content)}")

    @commands.command()
    async def chaddoge(self, ctx, *, content: commands.clean_content):
        stuff = content.split(',')
        first = stuff[0]
        second = stuff[1].strip() if len(stuff) == 2 else ''
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/chaddoge?chad={quote(first)}&virgin={quote(second)}")

    @commands.command()
    async def changemymind(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/changemymind?text={quote(content)}")

    @commands.command()
    async def doggo(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/doggo?text={quote(content)}")

    @commands.command()
    async def doggo(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/doggo?text={quote(content)}")

    @commands.command()
    async def handshake(self, ctx, *, content: commands.clean_content):
        stuff = content.split(',')
        first = stuff[0]
        second = stuff[1].strip() if len(stuff) <= 3 else ''
        third = stuff[2].strip() if len(stuff) <= 3 else ''
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/epichandshake?left={quote(first)}&right={quote(second)}&middle={quote(third)}")
    
    @commands.command()
    async def pooh(self, ctx, *, content: commands.clean_content):
        stuff = content.split(',')
        first = stuff[0]
        second = stuff[1].strip() if len(stuff) == 2 else ''
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/fancypooh?normal={quote(first)}&fancy={quote(second)}")

    @commands.command()
    async def gus(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/gus?text={quote(content)}")

    @commands.command()
    async def holdup(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/holdup?text={quote(content)}")

    @commands.command()
    async def lisa(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/lisa?text={quote(content)}")

    @commands.command()
    async def naruto(self, ctx, *, content: commands.clean_content):
        stuff = content.split(',')
        first = stuff[0]
        second = stuff[1].strip() if len(stuff) <= 3 else ''
        third = stuff[2].strip() if len(stuff) <= 3 else ''
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/narutohandshake?left={quote(first)}&right={quote(second)}&bottom={quote(third)}")
    
    @commands.command()
    async def pikachu(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/pikachu?text={quote(content)}")

    @commands.command()
    async def truth(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/scrolloftruth?text={quote(content)}")

    @commands.command()
    async def skinwalker(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/skinwalker?text={quote(content)}")

    @commands.command()
    async def burn(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/spongeburn?text={quote(content)}")

    @commands.command()
    async def boys(self, ctx, *, content: commands.clean_content):
        await ctx.embed(image_url = f"https://mime.rcp.r9n.co/memes/theboys?text={quote(content)}")

    