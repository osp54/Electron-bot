import nextcord
from nextcord.ext import commands
from utils.Button import notifyMemberBan

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id != 810758118442663936:
            return
        channel = self.bot.get_channel(844215222784753664)
        await channel.send(
            content= str(member) + " Вышел из сервера, желаете его забанить?",
            view=notifyMemberBan(member)
        )
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.channel.id != 878928850657112065:
            return
        if int(after.content.split()[1].replace("*", "")) >=10:
            await after.pin()

def setup(bot):
    bot.add_cog(darkdustry(bot))
