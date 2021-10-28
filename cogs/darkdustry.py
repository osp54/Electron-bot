import nextcord
from nextcord.ext import commands
from utils.Button import DarkdustryFAQButtons

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed = nextcord.Embed(
            title="FAQ - Часто задаваемые вопросы",
            description="1. Какой  IP у серверов?\n2. Как получить разбан?",
            color=0x3F00FF
        ).set_footer(text="Нажимайте на кнопки ниже что бы получить ответ на вопрос.")
    @commands.command()
    @commands.is_owner()
    async def faq_start(self, ctx):
        await ctx.send(embed=self.embed, view=DarkdustryFAQButtons())
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(897760744572063785)
        message = await channel.fetch_message(901168820285210674)
        await message.edit(embed=self.embed, view=DarkdustryFAQButtons())
def setup(bot):
    bot.add_cog(darkdustry(bot))
