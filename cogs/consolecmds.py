import nextcord
import os
from aioconsole import ainput
from colorama import Fore
from utils.misc import info, error, unload_extensions, load_extensions
from nextcord.ext import commands

class commandline(commands.Cog, name="commandline"):
    def __init__(self, bot):
        self.bot = bot
        self.cmds = {}
    def console_command(self, name, desc, usage="Not arguments..."):
        def decorator(func):
            self.cmds[name] = {"func": func, "desc": desc, "usage": usage}
            return func
        return decorator
    @console_command(name="reload", desc="Reload all cogs")
    async def reload(self, bot, ctx, text):
        info("Reloading cogs...")
        await unload_extensions(bot, "./cogs")
        await load_extensions(bot, "./cogs")
        
    async def exit(self, bot, ctx, text):
        await unload_extensions(bot, "./cogs")
        info("Closing bot...")
        await bot.close()
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
                    await self.cmds[cmd]["func"](self.bot, ctx, conl.replace(cmd, ""))
                else:
                    error(f"Command with name '{conl}' not found.")
            if conl.startswith("stop"):
                info("Stopped commands.")
                i = 0
            elif conl == "" or conl is None:
                pass
            elif conl.startswith("#"):
                pass
def setup(bot):
    bot.add_cog(commandline(bot))
