from discord.ext import commands
import discord, logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') #Writes log to file Discord.log
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!', description='Hi, I\'m a bot', help_attrs=dict(hidden=True))
#help_attrs -- hidden=True hides help from help message

@bot.event
async def on_ready():
    """ Prints login information when client is ready """
    print(f'==> Logged in as {bot.user.name}, id: {bot.user.id}')

@bot.event
async def on_message(message):
    """ Message event for client """
    if message.author.bot:
        return

    # this let's us define commands with the commands module
    return await bot.process_commands(message)

# get token from file
secret = ''
with open('secrets') as f:
    secret = f.readline().strip()

bot.load_extension('cogs.test')
bot.load_extension('cogs.quotes')
bot.load_extension('cogs.graphing')

bot.run(secret)
