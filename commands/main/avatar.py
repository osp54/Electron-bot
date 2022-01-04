import nextcord
from utils.bot import get_lang
from configparser import ConfigParser
from nextcord.ext import commands

b = ConfigParser
bot: commands.Bot = ""

@commands.command(name="avatar")
@commands.cooldown(1, 2, commands.BucketType.user)
async def avatar(ctx, member: nextcord.Member = None):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    if not member:
        member = ctx.message.author
    embed = nextcord.Embed(
        title=b.get('Bundle', 'embed.avatar.title').format(member),
        color=0x42F56C
    )
    embed.set_image(url=member.avatar.url)
    await ctx.send(embed=embed)

def setup(_bot):
    global bot
    bot = _bot
    return avatar