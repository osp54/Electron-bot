import nextcord
import time
from nextcord.ext import commands, tasks
from utils import MongoM
from utils.console import info, error
from datetime import datetime

class tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    async def check_unmutes(self):
        now = datetime.utcnow()
        unixnow = round(time.mktime(now.timetuple()))
        for mute in MongoM("muted_users").coll.find():
            if mute["muted_up"] >= unixnow:
                guild = self.bot.get_guild(mute["guild_id"])
                mutedm = guild.get_member(mute["user_id"])
                mute_role = await MongoM().getMuteRole(mute["guild_id"])
                await MongoM("muted_users").coll.delete_one({"guild_id": mute["guild_id"], "user_id": mute["user_id"]})
                try:
                    await mutedm.remove_roles(mute_role)
                except:
                    return

    @commands.Cog.listener()
    async def on_ready(self):
        await self.check_unmutes()
        
def setup(bot):
    bot.add_cog(tasks(bot))