import discord
import asyncio
import logging #imports Discord.py logging module
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') #Writes log to file Discord.log
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()

def example_func(author, message):
    client.send_message(message.channel, "%s, and eggs!" % author)

#client.event
def on_message(message):
    author = message.author
    if message.content.startswith('!spam'):
        example_func(author, message)
#pass Doyouevenpython1
async await client.login('MjY4ODI3OTY0NDQ2MDgxMDI0.C1la0w.-SNEYy_JrGB7PYfKONfc5bLrP1c')

client.run()
