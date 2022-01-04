import nextcord
from utils.bot import get_lang
from utils.other import format_name
from configparser import ConfigParser
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""

@commands.command(
    name="guild",
    aliases=["guildinfo", "сервер"]
)
@commands.cooldown(1, 2, commands.BucketType.user)
async def guild(ctx):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    guild = ctx.guild
    guild_owner = bot.get_user(guild.owner_id)

    features = "\n".join(format_name(f) for f in guild.features)

    embed = nextcord.Embed(title=guild.name, color=0x42F56C)
    embed.add_field(name="ID", value=int(guild.id))
    if guild_owner is not None:
        embed.add_field(name=b.get('Bundle', 'embed.guild.owner'), value=guild_owner)
    if guild.icon.url is not None:
        embed.add_field(name="Icon URL", value=f"[here]({guild.icon.url})")
    embed.add_field(name=b.get('Bundle', 'embed.guild.verefication.lvl'), value=str(guild.verification_level))
    embed.add_field(name=b.get('Bundle', 'embed.guild.members'), value=len(guild.members))
    if guild.premium_subscription_count is not None:
        embed.add_field(name=b.get('Bundle', 'embed.guild.boost.lvl'), value=guild.premium_tier)
        embed.add_field(name=b.get('Bundle', 'embed.guild.boosts'), value=guild.premium_subscription_count)
        embed.add_field(name=b.get('Bundle', 'embed.guild.boosters'), value=len(guild.premium_subscribers))
    embed.add_field(name=b.get('Bundle', 'embed.guild.channels'), value=len(guild.channels))
    embed.add_field(name=b.get('Bundle', 'embed.guild.text.channels'), value=len(guild.text_channels))
    embed.add_field(name=b.get('Bundle', 'embed.guild.voice.channels'), value=len(guild.voice_channels))
    embed.add_field(name=b.get('Bundle', 'embed.guild.categories'), value=len(guild.categories))
    embed.add_field(name=b.get('Bundle', 'embed.guild.roles'), value=len(guild.roles))
    embed.add_field(name=b.get('Bundle', 'embed.guild.emojis'), value=f"{len(guild.emojis)}/{guild.emoji_limit}")
    embed.add_field(name=b.get('Bundle', 'embed.guild.limit.file'),
                    value=f"{round(guild.filesize_limit / 1048576)} MB")
    embed.add_field(name=b.get('Bundle', 'embed.guild.features'), value=features)
    embed.set_thumbnail(url=guild.icon.url)
    await ctx.send(embed=embed)

def setup(_bot):
    global bot
    bot = _bot
    return guild