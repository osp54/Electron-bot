import nextcord
import pydustry
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server = pydustry.Server('mindurka.tk', server_port = 6567, socketinput_port = 6859)
    @commands.command()
    @commands.has_permission(administrator=True)
    async def restart(self, ctx):
        self.server.send_command('rr')
def setup(bot):
    bot.add_cog(darkdustry(bot))
