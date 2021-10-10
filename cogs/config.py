import pymongo
import nextcord
from utils.misc import get_lang
from nextcord.ext import commands
from configparser import ConfigParser

class config(commands.Cog, name="config"):
    def __init__(self, bot):
        self.bot = bot
        self.mclient = pymongo.MongoClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.collg = self.mclient.electron.guilds
        self.b = ConfigParser() # b - bundle
    @commands.group(name="config")
    @commands.has_permissions(manage_guild=True)
    async def config(self, ctx):
        if ctx.invoked_subcommand is None:
            self.b.read(f"locales/{get_lang(ctx.message)}.ini")
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.config.info.title'),
                description=self.b.get('Bundle', 'embed.config.info.desc').format("\n"),
                color=0x42F56C
            )
            await ctx.send(embed=embed)
    @config.command(name="config mute_role")
    @commands.has_permissions(manage_roles=True)
    async def mute_role(self, ctx, role: nextcord.Role):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        self.collg.update_one({"_id": ctx.guild.id}, {"$set": {'mute_role': role.id}})
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.mute-role-changed').format(role.mention),
            color=0x42F56C
        )
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(config(bot))
