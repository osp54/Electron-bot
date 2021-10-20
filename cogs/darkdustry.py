import nextcord
from nextcord.ext import commands
from utils.Button import DarkdustryFAQButtons

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = nextcord.Embed(
            title="Часто задаваемые вопросы",
            description="1. IP серверов",
            color=0x3F00FF
        )
    @commands.command()
    @commands.is_owner()
    async def faq_start(self, ctx):
        await ctx.send(embed=self.embed, view=darkdustryFAQButtons())
    @commands.Cog.listener()
    async def on_ready(self):
        pass
def setup(bot):
    bot.add_cog(darkdustry(bot))
