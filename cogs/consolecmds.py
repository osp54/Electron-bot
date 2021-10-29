import nextcord
import os
from aioconsole import ainput
from colorama import Fore
from utils.console import info, error
from utils.bot import unload_extensions, load_extensions
from nextcord.ext import commands

class commandline(commands.Cog, name="commandline"):
    def __init__(self, bot):
        self.bot = bot
        self.cmds = {
            "reload-all": {"func": reload_all, "desc": "Reload all cogs"},
            "exit": {"func": exit_bot, "desc": "Shutdown."}
        }
    async def reload_all(self, text):
        info("Reloading cogs...")
        await unload_extensions(bot, "./cogs")
        await load_extensions(bot, "./cogs")
        
    async def exit_bot(self, text):
        await unload_extensions(bot, "./cogs")
        info("Closing bot...")
        await bot.close()
    @commands.Cog.listener()
    async def on_ready(self, ctx):
        info("Console commands has started")
        while True:
            conl = await ainput(Fore.WHITE + ">" + Fore.RESET)
            for cmd in self.cmds:
                if conl.startswith(cmd):
                    await self.cmds[cmd]["func"](conl.replace(cmd, ""))
                else:
                    error(f"Command with name '{conl}' not found.")
            if conl.startswith("stop"):
                info("Stopped commands.")
                break
            elif conl == "" or conl is None:
                pass
            elif conl.startswith("#"):
                pass
def setup(bot):
    bot.add_cog(commandline(bot))
