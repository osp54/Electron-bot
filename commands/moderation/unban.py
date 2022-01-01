import nextcord
from configparser import ConfigParser
from utils.bot import get_lang
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""

@commands.cooldown(1, 2, commands.BucketType.user)
@commands.bot_has_permissions(ban_members=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, name_or_id, *, reason=None):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    ban = await ctx.get_ban(name_or_id)
    if not ban:
        return await ctx.send(b.get('Bundle', 'embed.user-not-found'))
    try:
        await ctx.guild.unban(ban.user, reason=reason)
    except:
        return
    await ctx.send(embed=nextcord.Embed(
        title=b.get('Bundle', 'embed.succerfully'),
        description=b.get('Bundle', 'embed.user-was-unbaned').format(ban.user),
        color=0x42F56C
    )
    )
    await ctx.message.add_reaction('✅')

def setup(_bot):
    global bot
    bot = _bot
    return unban