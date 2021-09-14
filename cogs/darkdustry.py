import nextcord
import pydustry
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class darkdustry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server = None
        self.servers = {
          'test':6567,
          'attack':6567,
          'surv':6567,
          'pvp':6567,
          'td':6567,
          'siege':6567
        }
    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.bot.get_channel(871410960986939473)
        self.server = pydustry.Server('localhost', server_port = 6567, socketinput_port = 7777)
        if message.author == self.bot.user:
            return
        if message.channel.id == channel.id:
            mmessage = message.content.replace("\n", " ")
            if '0000' in message.author.discriminator:
                return
            if '<' in mmessage and '>' in mmessage:
                return
            try:
                self.server.send_command(f'say {message.author} -› {mmessage}')
                await message.add_reaction('✅')
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                await channel.send(exception)
                await message.add_reaction('❌')
    @commands.command()
    @commands.has_role(869879808216150057)
    async def restart (self, ctx, server = None):
        if server is None:
            await ctx.send("Сервера: `sand`, `attack`, `surv`, `pvp`, `td`, `hexed`, `siege`")
            return
        try:
          self.server = pydustry.Server('localhost', server_port = self.servers[server], socketinput_port = 7777)
        except Exception, e:
          await ctx.send("Не правильно набранно название сервера")
          return
        self.server.send_command('rr')
        await ctx.send(f"Сервер `{self.server.get_status()['name']}` перезапущен!")
def setup(bot):
    bot.add_cog(darkdustry(bot))
