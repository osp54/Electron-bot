import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

class help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot
    pass
def setup(bot)
    bot.add_cog(help(bot))
