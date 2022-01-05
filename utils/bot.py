import os, re
import nextcord
from utils.console import error
from utils.mongo import MongoM
from configparser import ConfigParser

cp = ConfigParser()

def add_all_commands(bot):
    for dir in os.listdir("commands"):
        for file in os.listdir("commands/" + dir):
            if file.endswith(".py"):
                exec("from commands." + dir + " import " + file.replace(".py", "") + " as command")
                try:
                    bot.add_command(command.setup(bot))
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    error(f"Failed to load command {file}: {exception}")
def add_all_events(bot):
    for file in os.listdir("events"):
        if file.endswith(".py"):
            exec("from events import " + file.replace(".py", "") + " as event")
            try:
                bot.add_listener(event.setup(bot))
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to load event {file}: {exception}")
async def get_prefix(client, message, isInfo = False):
    if message.guild is None:
        return ""
    return await MongoM().getPrefix(message.guild.id)
    
async def get_lang(message):
    if message.guild is None:
        return "en"
    return await MongoM().getLang(message.guild.id)

async def localize(ctx, to_local, bundle="Bundle"):
    cp.read(f"locales/{await get_lang(ctx.message)}.ini")
    try:
        return cp.get(bundle, to_local)
    except:
        cp.read(f"locales/en.ini")
        return cp.get(bundle, to_local)

def format_duration_to_sec(time):
    time_list = re.split('(\d+)',time)
    time_in_s = None
    if time_list[2] == "s":
        time_in_s = int(time_list[1])
    if time_list[2] == "min":
        time_in_s = int(time_list[1]) * 60
    if time_list[2] == "h":
        time_in_s = int(time_list[1]) * 60 * 60
    if time_list[2] == "d":
        time_in_s = int(time_list[1]) * 60 * 60 * 24
    if time == 0 or time == "0":
        return "ND"
    return time_in_s
async def cmdInfo(ctx, bot, cmd):
        cp.read(f"locales/{await get_lang(ctx.message)}.ini")
        cmd = bot.get_command(cmd)
        embed = nextcord.Embed(
            title=cmd.name.capitalize(),
            description=cp.get("Bundle", f"{cmd}.description"),
            color=0x2B95FF
        ).add_field(
            name=cp.get("Bundle", "embed.help.usage"),
            value=cp.get("Bundle", f"{cmd}.usage")
        )
        if cmd.aliases is not None:
           embed.add_field(
                name=cp.get("Bundle", "embed.help.aliases"),
                value=", ".join(cmd.aliases)
            )
        await ctx.send(embed=embed)
