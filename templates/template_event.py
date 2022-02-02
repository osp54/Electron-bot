import nextcord
from nextcord.ext import commands
from configparser import ConfigParser

# для локализации
b = ConfigParser()

bot: commands.Bot = ""

@commands.Cog.listener("event")
async def event(event_options):
    pass

def setup(_bot):
    # получаем объект бота
    global bot
    bot = _bot
    # передаем ивент
    return event