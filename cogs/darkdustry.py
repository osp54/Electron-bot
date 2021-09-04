import nextcord
import pydustry
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server = pydustry.Server('localhost', server_port = 6567, socketinput_port = 7777)
    @commands.group()
    @commands.has_role(869879808216150057)
    async def server(self, ctx):
        pass
    @server.command()
    @commands.has_role(869879808216150057)
    async def test(self, ctx):
        self.server.send_command('rr')
def setup(bot):
    bot.add_cog(darkdustry(bot))
