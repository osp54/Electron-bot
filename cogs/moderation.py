
import discord
from discord.ext import commands

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot
    @bot.command()
    async def test(ctx):
        await ctx.send("test")
def setup(bot):
    bot.add_cog(moderation(bot))
