import nextcord
import datetime
from datetime import timedelta
from nextcord.ext import commands
from utils import MongoM
from utils.bot import get_lang
from utils.bot import format_duration_to_sec
from configparser import ConfigParser

b = ConfigParser()
bot: commands.Bot = ""

@commands.command(
    name="mute",
    aliases=['мьют', 'мут']
)
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.bot_has_permissions(manage_roles=True)
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: nextcord.Member, duration="0", *, reason="Not Specified"):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    guild = ctx.guild
    muted = True
    if ctx.author.id == member.id:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.error.mute.why-mute-myself'),
            color=0xE02B2B
        )
        await ctx.message.add_reaction('❌')
        return await ctx.send(embed=embed)
    if member.top_role.position > ctx.author.top_role.position or ctx.author.id != ctx.guild.owner.id:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.error.mute.role-above-or-equal'),
            color=0xE02B2B
        )
        await ctx.message.add_reaction('❌')
        return await ctx.send(embed=embed)
    if member.guild_permissions > ctx.author.guild_permissions:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.error.mute.role-above'),
            color=0xE02B2B
        )
        await ctx.message.add_reaction('❌')
        return await ctx.send(embed=embed)
    if format_duration_to_sec(duration) is None:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.error.mute.invalid-duration'),
            color=0xE02B2B
        )
        await ctx.message.add_reaction('❌')
        return await ctx.send(embed=embed)
    mute_role_id = await MongoM().getMuteRole(ctx.guild.id)
    mutedRole = guild.get_role(mute_role_id)
    if mutedRole is None:
        mutedRole = await guild.create_role(name="Electron Mute")
        await MongoM().setMuteRole(guild.id, mutedRole.id)
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                          read_messages=True)
    if format_duration_to_sec(duration) != "ND":
        await member.edit(timeout=datetime.datetime.utcnow() + timedelta(seconds=int(format_duration_to_sec(duration))))
    else:
        try:
            await member.add_roles(mutedRole, reason=f"{reason}({ctx.author})")
        except:
            muted = False
    if muted:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.succerfully'),
            description=b.get('Bundle', 'embed.mute.description').format(member.name),
            color=0x42F56C
        )
        embed.add_field(
            name=b.get('Bundle', 'embed.moderator'),
            value=ctx.message.author,
            inline=False
        )
        embed.add_field(
            name=b.get('Bundle', 'embed.reason'),
            value=reason,
            inline=False
        )
        if format_duration_to_sec(duration) != "ND":
            embed.add_field(
                name=b.get('Bundle', 'embed.duration'),
                value=str(timedelta(seconds=int(format_duration_to_sec(duration)))),
                inline=False
            )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')

def setup(_bot):
    global bot
    bot = _bot
    return mute
