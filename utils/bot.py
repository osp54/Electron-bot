import os
import nextcord
from utils.console import info, error
from utils.mongo import MongoM
from colorama import Fore
from configparser import ConfigParser

cp = ConfigParser()

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
        return self.b.get(bundle, to_local)

async def load_extensions(bot, dir):
    for file in os.listdir(dir):
        if file.endswith(".py") and not file.endswith("_.py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"{dir[2:]}.{extension}")
                info(f"Loaded extension {Fore.BLUE}{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to load extension {Fore.BLUE}{extension}{Fore.RESET}\n{exception}")

async def unload_extensions(bot, dir):
    for file in os.listdir(dir):
        if file.endswith(".py") and not file.endswith("_.py"):
            extension = file[:-3]
            try:
                bot.unload_extension(f"{dir[2:]}.{extension}")
                info(f"Unloaded extension {Fore.BLUE}{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to unload extension {Fore.BLUE}{extension}{Fore.RESET}\n{exception}")

async def cmdInfo(ctx, self, cmd):
        cp.read(f"locales/{await get_lang(ctx.message)}.ini")
        cmd = self.bot.get_command(cmd)
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
