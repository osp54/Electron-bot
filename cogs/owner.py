import discord
from discord.ext import commands
import os
import sys
class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot
    def restart_bot(): 
        os.execv(sys.executable, ['python'] + sys.argv)
    @commands.command(name="restart")
    @commands.is_owner()
    async def restart(self,ctx):
        embed = discord.Embed(
            title="Restarting...",
            description="Бот перезапускается...",
            color=0x42F56C
        )
        await ctx.send(embed=embed)
        restart_bot()
    @commands.command(name='embed')
    @commands.is_owner()
    async def embed(self, ctx,*, message):
        await ctx.message.delete()
        embed=discord.Embed(description=message, color=0xFF0000)
        await ctx.send(embed=embed)
    @commands.command(name='say')
    @commands.is_owner()
    async def say(self, ctx,*, message=None):
        await ctx.message.delete()
        await ctx.send(message)

def setup(bot):
    bot.add_cog(owner(bot))
