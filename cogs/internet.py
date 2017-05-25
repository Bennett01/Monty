from discord.ext import commands
from bs4 import BeautifulSoup
import discord, aiohttp

class Internet():

    def __init__(self, bot):
        self.bot = bot
        self.yt = 'https://www.youtube.com'

    @commands.command()
    async def youtube(self, *, search):
        """
        Searches YouTube for <search> linking the most relevant link.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.yt + f'/results?search_query={search}') as res:
                text = await res.read()
        html = BeautifulSoup(text, 'html.parser')
        top_link = html.find('a', class_='yt-uix-tile-link')
        link = top_link.get('href')

        await self.bot.say(self.yt + link)

    @commands.command(aliases=['lmtgfy', 'lmgtyf', 'lmtgyf'])
    async def lmgtfy(self, *, search):
        """
        Learn how to Google.
        """
        search_list = search.split(' ')
        search = '+'.join(search_list)
        await self.bot.say(f'https://lmgtfy.com/?q={search}')

def setup(bot):
    bot.add_cog(Internet(bot))
