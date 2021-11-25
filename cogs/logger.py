import nextcord
from datetime import datetime
from nextcord.ext import commands

class logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command(self, ctx):
        cch = self.bot.get_channel(913446383187554324)
        g_name = str(ctx.guild.name)
        g_id = "`"+str(ctx.guild.id)+"`"
        au_name = str(ctx.message.author)
        au_id = "`"+str(ctx.message.author.id)+"`"
        ch_name = str(ctx.channel)
        ch_id = "`"+str(ctx.channel.id)+"`"
        logem = nextcord.Embed(title="Console log "+str(datetime.now()),color=0xE4B400)
        logem.add_field(name="Guild",value=g_name+" \n"+g_id)
        logem.add_field(name="Author",value=au_name+" \n"+au_id)
        logem.add_field(name="Channel",value=ch_name+" \n"+ch_id)
        logem.add_field(name="Command",value=command)
        logem.add_field(name="Content",value=ctx.message.content, inline=False)
        await cch.send(embed=logem)
def setup(bot):
    bot.add_cog(logger(bot))
