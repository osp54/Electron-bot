from configparser import ConfigParser
from utils.bot import get_lang
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""

@commands.cooldown(1, 2, commands.BucketType.user)
async def ping(ctx):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    await ctx.send(b.get('Bundle', 'ping').format(round(bot.latency * 1000)))

def setup(_bot):
    global bot
    bot = _bot
    return ping