import nextcord
import os
from aioconsole import ainput
from colorama import Fore
from utils.misc import info, error
from nextcord.ext import commands

async def exit(self):
    unload_extensions(self.bot, "./cogs")
    info("Closing bot...")
    await self.bot.close()

class commandline(commands.Cog, name="commandline"):
    def __init__(self, bot):
        self.bot = bot
        self.cmds = {
             "exit": {"func": exit(), "desc": 0}
        }
    @commands.command()
    @commands.is_owner()
    async def start_console(self, ctx):
        i = 1
        await ctx.message.add_reaction("✅")
        info("Console commands has started")
        while i != 0:
            conl = await ainput(Fore.WHITE + ">" + Fore.RESET)
            for cmd in self.cmds:
                if conl.startswith(cmd):
                    cmd["func"](self)
            if conl.startswith("stop"):
                info("Stopped commands.")
                i = 0
            elif conl == "" or conl is None:
                pass
            elif conl.startswith("#"):
                pass
            else:
                error(f"Command with name '{conl}' not found.")
def setup(bot):
    bot.add_cog(commandline(bot))
