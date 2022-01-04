import nextcord
import os
from configparser import ConfigParser
from utils.bot import cmdInfo, get_prefix, get_lang
from nextcord.ext import commands

bot: commands.Bot = ""
b = ConfigParser()

@commands.command(name="help", aliases=['хелп', 'помощь'])
@commands.cooldown(1, 2, commands.BucketType.user)
async def help(ctx, command=None):
    b.read(f"locales/{await get_lang(ctx.message)}.ini")
    if command is None:
        embed = nextcord.Embed(title=b.get("Bundle", "embed.help.title"),
                               description=b.get("Bundle", "embed.help.description"), color=0xE4B400)
        for dir in os.listdir("commands"):
            if dir != "owner":
                os.rmdir("commands/" + dir + "/__pycache__")
                cmds = ", ".join(os.listdir("commands/" + dir)).replace(".py", "")
                embed.add_field(name=b.get("Bundle", "embed.help." + dir), value=cmds, inline=False)
        await ctx.send(embed=embed)
    else:
        await cmdInfo(ctx, bot, command)


def setup(_bot):
    global bot
    bot = _bot
    return help