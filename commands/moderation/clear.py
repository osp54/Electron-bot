import nextcord
from configparser import ConfigParser
from utils.bot import get_lang
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""

@commands.command(
    name="clear",
    aliases=['очистить']
)
@commands.cooldown(1, 2, commands.BucketType.user)
@commands.bot_has_permissions(manage_messages=True)
@commands.has_permissions(manage_messages=True, manage_channels=True)
async def clear(ctx, amount):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    try:
        amount = int(amount)
    except:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.clear.not-amount').format(amount),
            color=0xE02B2B
        )
        await ctx.send(embed=embed)
        return await ctx.message.add_reaction('❌')
    if amount < 1:
        embed = nextcord.Embed(
            title=b.get('Bundle', 'embed.error'),
            description=b.get('Bundle', 'embed.clear.not-amount').format(amount),
            color=0xE02B2B
        )
        await ctx.send(embed=embed)
        return await ctx.message.add_reaction('❌')
    purged_messages = await ctx.message.channel.purge(limit=amount)
    embed = nextcord.Embed(
        title=b.get('Bundle', 'embed.succerfully'),
        description=b.get('Bundle', 'embed.clear.purged').format(ctx.author, len(purged_messages)),
        color=0x42F56C
    )
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')

def setup(_bot):
    global bot
    bot = _bot
    return clear