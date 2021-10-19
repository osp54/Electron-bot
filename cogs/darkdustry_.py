import nextcord
from nextcord.ext import commands

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.is_owner()
    async def faq_start(self, ctx):
        embed = nextcord.Embed(
            title="Часто задаваемые вопросы",
            description="1. хз\n2.хзхз",
            color=0x3F00FF
        )
        await ctx.send(embed=embed, view=None)
def setup(bot):
    bot.add_cog(darkdustry(bot))
