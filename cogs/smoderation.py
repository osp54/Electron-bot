import nextcord
from dislash import slash_command, ActionRow
from nextcord.ext import commands

class slashmoderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command(description="Тест")
    async def hello(self, inter):
        await inter.respond("Оно работает!")
def setup(bot):
    bot.add_cog(slashmoderation(bot))
