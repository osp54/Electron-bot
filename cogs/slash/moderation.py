
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class slashmoderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(slashmoderation(bot))
