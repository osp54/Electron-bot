import nextcord
from configparser import ConfigParser
from utils.bot import get_lang
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""

@commands.command(
    name="slowmode",
    alias=['слоумод']
)
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.has_permissions(manage_channels=True)
@commands.bot_has_permissions(manage_channels=True)
async def command(ctx, slowmode: int = None, channel: nextcord.TextChannel = None):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    if channel is None:
        channel = ctx.channel
    slowmode = max(min(slowmode, 21600), 0)
    await channel.edit(slowmode_delay=slowmode)
    embed = nextcord.Embed(
        title=b.get('Bundle', 'embed.succerfully'),
        description=b.get('Bundle', 'embed.slowmode.done').format(slowmode),
        color=0x00ff82
    )
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

