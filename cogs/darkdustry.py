import nextcord
from nextcord.ext import commands
from utils.Button import DarkdustryFAQButtons

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = nextcord.Embed(
            title="FAQ - Часто задаваемые вопросы",
            description="1. Какой  IP у серверов?\n2. Скоро",
            color=0x3F00FF
        )
    @commands.command()
    @commands.is_owner()
    async def faq_start(self, ctx):
        await ctx.send(embed=self.embed, view=DarkdustryFAQButtons())
    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(810758118442663936)
        channel = guild.fetch_channel(897760744572063785)
        message = channel.fetch_message(901168820285210674)
        await message.edit(embed=self.embed, view=DarkdustryFAQButtons())
def setup(bot):
    bot.add_cog(darkdustry(bot))
