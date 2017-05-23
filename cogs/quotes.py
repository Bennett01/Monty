from discord.ext import commands
import discord
import json
import random

class Quotes():

    def __init__(self, bot):
        self.bot = bot
        with open('quotes.json') as f:
            self.quotes = json.load(f)

    @commands.command(name='import')
    async def quote(self, module):
        """ Prints quotes from quotes.json """
        if module == 'this':
            return await self.bot.say(self.quotes['zen'])
        if module.lower() == 'monty':
            i = random.randint(0, len(self.quotes['monty']) - 1)
            return await self.bot.say(self.quotes['monty'][i])

def setup(bot):
    bot.add_cog(Quotes(bot))
