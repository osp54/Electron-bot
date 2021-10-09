import nextcord
from utils.misc import info
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
            conl = input().split()
            if conl[1] = "eval"
                eval("".join(conl))
def setup(bot):
    bot.add_cog(commandline(bot))
