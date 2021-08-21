import discord
from discord.ext import commands
import os
import pendulum
import sys
class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot
    def info(desc):
        now = pendulum.now('Europe/Moscow')
        print(f"{Fore.BLUE}[{Fore.RESET}{now.day}:{now.hour}:{now.minute}:{now.second}{Fore.BLUE}] " + Fore.BLUE + f"[I] {Fore.RESET}" + desc)
    def error(desc):
        now = pendulum.now('Europe/Moscow')
        print(f"{Fore.RED}[{Fore.RESET}{now.day}:{now.hour}:{now.minute}:{now.second}{Fore.RED}] " + Fore.RED + f"[E] {Fore.RESET}" + desc)

    @commands.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, dir, cog):
        try:
            self.bot.load_extension(f"{dir[2:]}.{cog}")
            info(f"Loaded extension {cog}")
            await ctx.send("Готово!")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            error(f"Failed to load extension {cog}\n{exception}")
    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        await ctx.send("\n".join(bot.guilds))
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
