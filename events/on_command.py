import nextcord
from nextcord.ext import commands
from utils import MongoM
from configparser import ConfigParser

b = ConfigParser()
bot: commands.Bot = ""

@commands.Cog.listener()
async def on_command(ctx):
    await MongoM().coll.update_one({"_id": 872078273553764372}, {"$inc": {"executed_cmds": 1}})
    channel = bot.get_channel(913446383187554324)
    embed = nextcord.Embed(title="Console log", color=0xE4B400)
    embed.add_field(name="Guild", value=ctx.guild.name + " \n" + str(ctx.guild.id))
    embed.add_field(name="Author", value=str(ctx.author) + " \n" + str(ctx.author.id))
    embed.add_field(name="Channel", value=ctx.channel.name + " \n" + ctx.channel.id)
    embed.add_field(name="Command", value=ctx.message.content, inline=False)
    await channel.send(embed=embed)


def setup(_bot):
    global bot
    bot = _bot
    return on_command