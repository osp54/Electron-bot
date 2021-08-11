import discord
from discord.ext import commands

class anti_scam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx, message):
        #TODO
def setup(bot):
    bot.add_cog(anti_scam(bot))
