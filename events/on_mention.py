import nextcord
from utils.bot import get_lang, get_prefix
from nextcord.ext import commands
from configparser import ConfigParser

b = ConfigParser()
bot: commands.Bot = ""

@commands.Cog.listener('on_message')
async def on_mention(message):
    electron = ['electron', 'электрон']
    b.read(f"locales/{await get_lang(message)}.ini")
    if '<@861541287161102376>' == message.content:
        prefix = await get_prefix(bot, message, True)
        await message.reply(b.get('Bundle', 'HelloMessage').format(prefix), mention_author=False)
    for i in electron:
        if i in message.content.lower():
            await message.add_reaction("⚡")

def setup(_bot):
    global bot
    bot = _bot
    return on_mention