import colorama
import pendulum
import pymongo
import os
import nextcord
import json
from nextcord.ext.commands import when_mentioned_or
from configparser import ConfigParser
from colorama import init, Fore, Back, Style

mclient = pymongo.MongoClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mclient.electron
collg = db.guilds

def get_prefix2(client, message, isInfo = False):
    res = collg.find_one({"_id": message.guild.id})
    return res["prefix"]
    
def get_lang(message):
    res = collg.find_one({"_id": message.guild.id})
    return res["lang"]

def localize(ctx, self, to_local, bundle="Bundle"):
    self.b.read(f"locales/{get_lang( ctx.message)}.ini")
    try:
        return self.b.get(bundle, to_local)
    except:
        self.b.read(f"locales/en.ini")
        return self.b.get(bundle, to_local)
async def cmdInfo(ctx, self, cmd):
        ConfigParser().read(f"locales/{get_lang(ctx.message)}.ini")
        try:
            cmd = self.bot.get_command(cmd)
        except:
            eembed = nextcord.Embed(
                title=self.b.get("Bundle", "embed.error"),
                description=self.b.get("Bundle", "error.embed.command.not.found"),
                color=0xFF0000
            )
            return await ctx.send(embed=eembed)
        embed = nextcord.Embed(
            title=cmd.name.capitalize(),
            description=self.b.get("Bundle", f"{cmd}.description"),
            color=0x2B95FF
        ).add_field(
            name=self.b.get("Bundle", "embed.help.usage"),
            value=self.b.get("Bundle", f"{cmd}.usage")
        )
        aliase = '('
        for alias in cmd.aliases:
            aliase += f" `{alias}` "
        embed.add_field(
            name=self.b.get("Bundle", "embed.help.aliases"),
            value=f"{aliase})"
        )
        await ctx.send(embed=embed)
#загрузить все расширения из папки
def load_extensions(bot, dir):
    for file in os.listdir(dir):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"{dir[2:]}.{extension}")
                info(f"Loaded extension {Fore.BLUE}{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to load extension {Fore.BLUE}{extension}{Fore.RESET}\n{exception}")

def unload_extensions(bot, dir):
    for file in os.listdir(dir):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.unload_extension(f"{dir[2:]}.{extension}")
                info(f"Unloaded extension {Fore.BLUE}{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                error(f"Failed to unload extension {Fore.BLUE}{extension}{Fore.RESET}\n{exception}")

def info(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.WHITE}[{now.day}:{now.hour}:{now.minute}:{now.second}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
def error(desc):
    now = pendulum.now('Europe/Moscow')
    print(f"{Fore.WHITE}[{now.day}:{now.hour}:{now.minute}:{now.second}] " + Fore.RED + f"[E] " + desc)

def format_name(name: str) -> str:
    return name.replace("_", " ").title().strip()
