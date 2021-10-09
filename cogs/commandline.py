import nextcord
from utils.misc import info, error
from nextcord.ext import commands

class commandline(commands.Cog, name="commandline"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.is_owner()
    async def start_console(self, ctx):
        i = 1
        await ctx.message.add_reaction("✅")
        info("Console commands has started")
        while i != 0:
            conl = input(">")
            if conl.startswith("exit"):
                unload_extensions(self.bot, "./cogs")
                await self.bot.close()
            elif conl.startswith("stop"):
                info("Stopped commands.")
                i = 0
            else:
                error("Command not found")
def setup(bot):
    bot.add_cog(commandline(bot))
