from configparser import  ConfigParser
from nextcord.ext import commands

# для локализации
b = ConfigParser()

bot: commands.Bot = ""

@commands.command()
async def command(ctx, options):
    pass

def setup(_bot):
    # получаем объект бота
    global bot
    bot = _bot
    # передаем ивент
    return command