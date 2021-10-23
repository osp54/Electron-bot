import nextcord
from nextcord.ext import commands, tasks
from utils.misc import info, error

class _topgg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=30)
    async def update_stats(self):
        try:
            await self.bot.topggpy.post_guild_count()
            info(f"[Topgg]Posted server count ({self.bot.topggpy.guild_count})")
        except Exception as e:
            error(f"[Topgg]Failed to post server count\n{e.__class__.__name__}: {e}")

def setup(bot):
    bot.add_cog(_topgg(bot))