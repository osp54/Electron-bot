import nextcord
from configparser import ConfigParser
from utils.bot import get_lang
from nextcord.ext import commands

b = ConfigParser()
bot = ""

@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_channels=True)
@commands.bot_has_permissions(manage_channels=True)
async def clone(ctx, channel: nextcord.TextChannel = None):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    if channel is None:
        channel = ctx.channel
    await channel.clone(reason=ctx.author)
    await ctx.send(b.get('Bundle', 'embed.clone.cloned').format(channel.mention))

def setup(_bot):
    global bot
    bot = _bot
    return clone