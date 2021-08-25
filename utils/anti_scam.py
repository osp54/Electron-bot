import discord
from discord.ext import commands

scam_links = ["steamcommunity.link", "discorcl.link", "steamcommunity.com.ru", "steamcommunnity.ru", "steamccommunity.com.ru", "steamcommuunity.com.ru", "surl.li", "stearncornmrunity.ru.com", "fustcup.ru", "steamcommrunity.com", "brapo.space", "steamcommunutiy.com"]

class anti_scam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        for link in scam_links:
            if link in message.content:
                await message.delete()
        #TODO: больше скам ссылок
def setup(bot):
    bot.add_cog(anti_scam(bot))
