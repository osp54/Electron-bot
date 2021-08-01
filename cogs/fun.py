import discord
from discord.ext import commands

class fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='embed')
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx,*, message):
        """
        Отправить эмбед сообщение
        """
        await ctx.message.delete()
        embed=discord.Embed()
        embed.add_field(name="Embed", value=f"{message}", inline=False)
        await ctx.send(embed=embed)
    @commands.command(name='say')
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx,*, message=None):
        """
        Отправить сообщение от имени бота
        """
        await ctx.message.delete()
        await ctx.send(message)
def setup(bot):
    bot.add_cog(fun(bot))
