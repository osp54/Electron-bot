import discord
from discord.ext import commands

class anti_scam(commands.Cog, name="anti_scam"):
    def __init__(self, bot):
        self.bot = bot
    

def setup(bot):
    bot.add_cog(anti_scam(bot))
