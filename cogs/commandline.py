import nextcord
from utils.misc import info, error, unload_extensions
from nextcord.ext import commands

class commandline(commands.Cog, name="commandline"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.is_owner()
    async def start_console(self, ctx):
        await ctx.message.add_reaction("✅")
        info("Console commands has started")
        while True:
            conl = input()
            if conl.startswith("eval"):
                exec(conl.replace("eval", ""))
            elif conl.startswith("exit"):
                unload_extensions(self.bot, "./cogs")
                await self.bot.close()
            else:
                error("Command not found")
def setup(bot):
    bot.add_cog(commandline(bot))
