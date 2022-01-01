import nextcord
from configparser import ConfigParser
from utils.bot import get_lang
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""

@commands.cooldown(1, 2, commands.BucketType.user)
@commands.bot_has_permissions(kick_members=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: nextcord.Member, *, reason="Not Specified"):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    if ctx.author.id == member.id:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.error.kick.why-kick-myself'),
            color=0xE02B2B
        )
        await ctx.message.add_reaction('❌')
        return await ctx.send(embed=embed)
    if member.top_role.position >= ctx.author.top_role.position:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.error.kick.role-above-or-equal'),
            color=0xE02B2B
        )
        await ctx.message.add_reaction('❌')
        return await ctx.send(embed=embed)
    if member.guild_permissions > ctx.author.guild_permissions:
        embed = nextcord.Embed(
            title='Ошибка',
            description=b.get('Bundle', 'embed.error.kick.role-above'),
            color=0xE02B2B
        )
        await ctx.message.add_reaction('❌')
        return await ctx.send(embed=embed)
    await member.kick(reason=f"{reason}({ctx.message.author})")
    embed = nextcord.Embed(
        title=b.get('Bundle', 'embed.succerfully'),
        description=b.get('Bundle', 'embed.kick.kicked').format(member),
        color=0x42F56C
    ).add_field(
        name=b.get('Bundle', 'embed.moderator'),
        value=ctx.message.author
    ).add_field(
        name=b.get('Bundle', 'embed.reason'),
        value=reason
    )
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

def setup(_bot):
    global bot
    bot = _bot
    return kick