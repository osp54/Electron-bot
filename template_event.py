import nextcord
from nextcord.ext import commands
from configparser import ConfigParser

b = ConfigParser()
bot: commands.Bot = ""

@commands.Cog.listener("event")
async def event(event_options):
    pass

def setup(_bot):
    global bot
    bot = _bot
    return event