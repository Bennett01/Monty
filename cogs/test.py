from discord.ext import commands
import discord

class Test():

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self):
        return await self.bot.say('Hello I am Monty the Python bot')

    @commands.command(pass_context=True)
    async def spam(self, ctx, member = None):
        if member is None:
            member = ctx.message.author
        return await self.bot.say(f'{member}, and eggs!')

def setup(bot):
    bot.add_cog(Test(bot))
