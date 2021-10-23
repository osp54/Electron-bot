import nextcord
import topgg
from nextcord.ext import commands, tasks
from utils.misc import info, error

class _topgg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.topggpy = topgg.DBLClient(self.bot, "https://top.gg/bot/861541287161102376/webhooks")

    @tasks.loop(minutes=30)
    async def update_stats(self):
        try:
            await self.topggpy.post_guild_count()
            info(f"[Topgg]Posted server count ({self.topggpy.guild_count})")
        except Exception as e:
            error(f"[Topgg]Failed to post server count\n{e.__class__.__name__}: {e}")
    @commands.Cog.listener()
    async def on_ready(self):
        self.update_stats.start()
def setup(bot):
    bot.add_cog(_topgg(bot))