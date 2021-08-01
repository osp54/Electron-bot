
import discord
from discord.ext import commands

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot
   @commands.command(name='mute')
   @commands.has_permissions(kick_members=True)
   async def mute(ctx, member: discord.Member):
       try:
           role = discord.utils.get(member.server.roles, name='Muted')
           await ctx.add_roles(member, role)
           embed=discord.Embed(title="Юзер замьючен!", description="**{0}** был замьючен модератором**{1}**!".format(member, ctx.message.author), color=0xff00f6)
           await ctx.send(embed=embed)
       except:
           await ctx.send("У вас недостаточно прав для этой команды.")
def setup(bot):
    bot.add_cog(moderation(bot))
