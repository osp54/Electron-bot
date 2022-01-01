import nextcord
from utils import MongoM
from configparser import ConfigParser
from utils.bot import get_lang
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""

@commands.command(
    name="unmute",
    aliases=['размьют', 'размут']
)
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.bot_has_permissions(manage_roles=True)
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: nextcord.Member):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    unmuted = True
    if ctx.author.id == member.id:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.error.unmute.not-unmute-myself'),
            color=0xE02B2B
        )
        await ctx.send(embed=embed)
        return await ctx.message.add_reaction('❌')
    mutedRole = ctx.guild.get_role(await MongoM().getMuteRole(ctx.guild.id))
    try:
        await member.remove_roles(mutedRole, reason=ctx.author)
    except:
        unmuted = False
    try:
        await member.edit(timeout=None)
    except:
        unmuted = False
    if unmuted:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.succerfully'),
            description=b.get('Bundle', 'embed.unmute.unmuted').format(member),
            color=0x42F56C
        ).add_field(name=b.get('Bundle', 'embed.moderator'), value=ctx.message.author)
        await ctx.send(embed=embed)

def setup(_bot):
    global bot
    bot = _bot
    return unmute