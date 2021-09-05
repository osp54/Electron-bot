import nextcord
import pydustry
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server = None
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.content, str):
            return
        if message.author.discriminator == 0000:
            return
        channel = self.bot.get_channel(871410960986939473)
        self.server = pydustry.Server('localhost', server_port = 6567, socketinput_port = 7777)
        if message.channel.id == channel.id:
            self.server.send_command(f'say {message.author} -› {message.content}')
    @commands.command()
    @commands.has_role(869879808216150057)
    async def restart (self, ctx, server = None):
        if server is None:
            await ctx.send("Сервера: `sand`, `attack`, `surv`, `pvp`, `td`, `hexed`, `siege`")
        elif server == 'test':
            self.server = pydustry.Server('localhost', server_port = 6567, socketinput_port = 7777)
        elif server == 'attack':
            self.server = pydustry.Server('localhost', server_port = 6567, socketinput_port = 7777)
        elif server == 'surv':
            self.server = pydustry.Server('localhost', server_port = 6567, socketinput_port = 7777)
        elif server == 'pvp':
            self.server = pydustry.Server('localhost', server_port = 6567, socketinput_port = 7777)
        elif server == 'td':
            self.server = pydustry.Server('localhost', server_port = 6567, socketinput_port = 7777)
        elif server == 'siege':
            self.server = pydustry.Server('localhost', server_port = 8000, socketinput_port = 8001)
        self.server.send_command('rr')
        await ctx.send(f"Сервер `{self.server.get_status()['name']}` перезапущен!")
def setup(bot):
    bot.add_cog(darkdustry(bot))
