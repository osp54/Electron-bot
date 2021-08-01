import discord
from discord.ext import commands

class moderation(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='embed')
    async def embed(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed()
        embed.add_field(name="Embed", value=f"{message}", inline=False)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(fun(bot))
