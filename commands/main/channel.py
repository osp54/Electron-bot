import nextcord
import humanize
import datetime
from utils.bot import get_lang
from configparser import ConfigParser
from nextcord.ext import commands

b = ConfigParser()
bot: commands.Bot = ""


@commands.command(
    name="channel",
    aliases=['канал', 'channelinfo']
)
async def channel(ctx, channel: nextcord.TextChannel = None):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    channel = channel or ctx.channel
    embed = nextcord.Embed(title=b.get('Bundle', 'embed.channel').format(channel), color=0x42F56C)
    if channel.topic:
        embed.add_field(name=b.get('Bundle', 'embed.channel.desc'), value=channel.topic, inline=False)
    embed.add_field(
        name=b.get('Bundle', 'embed.channel.when.created'),
        value=f'{nextcord.utils.format_dt(channel.created_at, "F")}  ({nextcord.utils.format_dt(channel.created_at, "R")})',
    )
    embed.add_field(name="ID", value=channel.id)
    embed.add_field(name=b.get('Bundle', 'embed.channel.type'), value=channel.type)
    embed.add_field(name=b.get('Bundle', 'embed.channel.position'),
                    value=f"{channel.position}/{len(ctx.guild.text_channels)}")
    embed.add_field(name=b.get('Bundle', 'embed.channel.category'), value=channel.category.name)
    if channel.slowmode_delay:
        embed.add_field(
            name=b.get('Bundle', 'embed.channel.slowmode.title'),
            value=f"{channel.slowmode_delay} sec ({humanize.naturaldelta(datetime.timedelta(seconds=int(channel.slowmode_delay)))})",
        )

    await ctx.send(embed=embed)


def setup(_bot):
    global bot
    bot = _bot
    return channel