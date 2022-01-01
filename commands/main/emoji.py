import nextcord
from utils.bot import get_lang
from configparser import ConfigParser
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""


@commands.cooldown(1, 2, commands.BucketType.user)
async def emoji( ctx, emoji: nextcord.Emoji):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    embed = nextcord.Embed(title=b.get('Bundle', 'embed.emoji.title').format(emoji.name), color=0x42F56C)
    embed.set_thumbnail(url=emoji.url)
    embed.set_image(url=emoji.url)
    embed.add_field(name="ID", value=emoji.id)
    if emoji.user:
        embed.add_field(name=b.get('Bundle', 'embed.emoji.who.author.emoji'), value=emoji.user)
    embed.add_field(name=b.get('Bundle', 'embed.emoji.server'), value=emoji.guild)
    embed.add_field(
        name=b.get('Bundle', 'embed.emoji.whencreated'),
        value=f'{nextcord.utils.format_dt(emoji.created_at, "F")} ({nextcord.utils.format_dt(emoji.created_at, "R")})',
    )
    embed.add_field(name="URL", value=f"[Here]({emoji.url})")
    await ctx.send(embed=embed)

def setup(_bot):
    global bot
    bot = _bot
    return emoji