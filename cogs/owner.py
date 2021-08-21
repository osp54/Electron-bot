import discord
from discord.ext import commands
import os
import sys
from bot import info, error
class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='load')
    async def load(self, ctx, dir, cog)
        try:
            self.bot.load_extension(f"{dir[2:]}.{cog}")
            info(f"Loaded extension {cog}")
            await ctx.send("Готово!")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            error(f"Failed to load extension {cog}\n{exception}")
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
