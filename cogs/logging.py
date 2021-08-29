import nextcord
from nextcord.ext import commands
from functions import error, info
class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        info(f"Added new guild! Name: {guild.name}, members: {guild.member_count}.")
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        info(f"Removed guild. Name: {guild.name}, members: {guild.member_count}.")
def setup(bot):
    bot.add_cog(owner(bot))
