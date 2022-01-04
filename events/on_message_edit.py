from nextcord.ext import commands
from utils.bot import get_prefix
from configparser import ConfigParser

b = ConfigParser()
bot: commands.Bot = ""

@commands.Cog.listener()
async def on_message_edit(old, new):
    try:
        if new.content.startswith(await get_prefix(bot, new)):
            await bot.process_commands(new)
    except:
        return

def setup(_bot):
    global bot
    bot = _bot
    return on_message_edit