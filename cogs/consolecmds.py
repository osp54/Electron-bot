import nextcord
import os
from aioconsole import ainput
from colorama import Fore
from utils.console import info, error, colored
from utils.bot import unload_extensions, load_extensions
from nextcord.ext import commands

async def reload_all(bot, text):
    info("Reloading cogs...")
    await unload_extensions(bot, "./cogs")
    await load_extensions(bot, "./cogs")
        
async def exit_bot(bot, text):
    await unload_extensions(bot, "./cogs")
    info("Closing bot...")
    await bot.close()

class commandline(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cmds = {
            "reload-all": {
                "name": "reload-all",
                "func": reload_all,
                "desc": "Reload all bot cogs.",
                "usage": "Without arguments"
            },
            "exit": {
                "name": "exit",
                "func": exit_bot, 
                "desc": "Shutdown process and bot.",
                "usage": "Without arguments"
            }
        }
    @commands.Cog.listener()
    async def on_ready(self, ctx):
        info("Console commands has started")
        while True:
            conl = await ainput(Fore.WHITE + ">" + Fore.RESET)
            for cmd in self.cmds:
                if conl.startswith(cmd):
                    await self.cmds[cmd]["func"](self.bot, conl.replace(f"{cmd} ", ""))
                elif conl.startswith("stop"):
                    info("Stopped")
                    break
                elif conl == "" or conl is None:
                    pass
                elif conl.startswith("#"):
                    pass
                elif conl.startswith("help"):
                    text = ""
                    for cmd in self.cmds:
                        text += colored(self.cmds[cmd]["name"]) + " - " \
                            + "Usage: " + colored(self.cmds[cmd]["usage"]) \
                            + " Description: " + colored(self.cmds[cmd]["desc"]) + "\n"
                    print(text)
                else:
                    error(f"Command with name '{conl}' not found.")
def setup(bot):
    bot.add_cog(commandline(bot))
