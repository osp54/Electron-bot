import nextcord
from nextcord.ext import commands
from colorama import init, Fore, Back, Style
from utils.misc import error, info
class logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        info(f"Added new guild! Name: {Fore.CYAN}{guild.name}{Fore.RESET}, members: {Fore.CYAN}{guild.member_count}")
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        info(f"Removed guild. Name: {Fore.CYAN}{guild.name}{Fore.RESET}, members: {Fore.CYAN}{guild.member_count}")
def setup(bot):
    bot.add_cog(logging(bot))
