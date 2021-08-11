import discord
from discord.ext import commands
import os
import sys
import json
with open("owners.json") as file:
    owners = json.load(file)
class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='embed')
    async def embed(self, ctx,*, message):
        if ctx.message.author.id in owners["owners"]:
            await ctx.message.delete()
            embed=discord.Embed()
            embed.add_field(value=f"{message}", inline=False)
            await ctx.send(embed=embed)
    @commands.command(name='say')
    async def say(self, ctx,*, message=None):
        if ctx.message.author.id in owners["owners"]:
            await ctx.message.delete()
            await ctx.send(message)

def setup(bot):
    bot.add_cog(owner(bot))
