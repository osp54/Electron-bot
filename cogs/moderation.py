
import discord
from discord.ext import commands

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(moderation(bot))
