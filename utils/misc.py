import colorama
import motor
import os
import nextcord
import json
from datetime import datetime
from configparser import ConfigParser
from colorama import init, Fore, Back, Style

cp = ConfigParser()
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
collg = client.electron.guilds

def get_prefix2(client, message, isInfo = False):
    res = await collg.find_one({"_id": message.guild.id})
    return res["prefix"]
    
def get_lang(message):
    res = await collg.find_one({"_id": message.guild.id})
    return res["lang"]

def localize(ctx, to_local, bundle="Bundle"):
    cp.read(f"locales/{get_lang(ctx.message)}.ini")
    try:
        return cp.get(bundle, to_local)
    except:
        cp.read(f"locales/en.ini")
        return self.b.get(bundle, to_local)
async def cmdInfo(ctx, self, cmd):
        cp.read(f"locales/{get_lang(ctx.message)}.ini")
        cmd = self.bot.get_command(cmd)
        embed = nextcord.Embed(
            title=cmd.name.capitalize(),
            description=cp.get("Bundle", f"{cmd}.description"),
            color=0x2B95FF
        ).add_field(
            name=cp.get("Bundle", "embed.help.usage"),
            value=cp.get("Bundle", f"{cmd}.usage")
        )
        aliase = '('
        for alias in cmd.aliases:
            aliase += f" `{alias}` "
        embed.add_field(
            name=cp.get("Bundle", "embed.help.aliases"),
            value=f"{aliase})"
        )
        await ctx.send(embed=embed)
#загрузить все расширения из папки
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

def info(desc):
    now = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    print(f"{Fore.WHITE}[{now}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
    print(f"{Fore.WHITE}[{now}] " + Fore.RED + f"[E] " + desc)

def format_name(name: str) -> str:
    return name.replace("_", " ").title().strip()
