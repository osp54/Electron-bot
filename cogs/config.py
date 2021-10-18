import nextcord
from utils.mongo import MongoM
from utils.misc import get_lang
from utils.Button import SetLangButton
from nextcord.ext import commands
from configparser import ConfigParser

class config(commands.Cog, name = "config"):
    def __init__(self, bot):
        self.bot = bot
        self.maxcharsprefix = 8
        self.b = ConfigParser() # b - bundle
    @commands.group(name = "config")
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_guild = True)
    async def config(self, ctx):
        if ctx.invoked_subcommand is None:
            mute_role = await MongoM().getMuteRole(ctx.guild.id)
            prefix = await MongoM().getPrefix(ctx.guild.id)
            lang = await MongoM().getLang(ctx.guild.id)
            anti_scam = await MongoM().checkAntiScam(ctx.guild.id)
            self.b.read(f"locales/{await get_lang(ctx.message)}.ini")
            embed = nextcord.Embed(
                title = self.b.get('Bundle', 'embed.config.info.title'),
                description = self.b.get('Bundle', 'embed.config.info.desc').format(prefix, lang, f"<@&{mute_role}>", anti_scam, "\n"),
                color = 0x42F56C
            )
            await ctx.send(embed = embed)
    @config.command(name='prefix', aliases=['префикс'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def prefix(self, ctx, prefix):
        self.b.read(f"locales/{await get_lang(ctx.message)}.ini")
        if await get_prefix2(self.bot, ctx.message) == prefix:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'error.embed.same.prefix.description'),
                color=0xE02B2B
            )
            return await ctx.send(embed=embed)
        if len(prefix) >= self.maxcharsprefix:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'error.embed.max.num.of.chars.in.prefix.description').format(self.maxcharsprefix),
                color=0xE02B2B
            )
            return await ctx.send(embed=embed)
        await MongoM().setPrefix(ctx.guild.id, prefix)
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.prefixchanged.description').format(prefix,),
            color=0x42F56C
        ).set_footer(text=self.b.get('Bundle', 'embed.prefix.prompt'))
        await ctx.send(embed=embed)
        await ctx.guild.me.edit(nick=f"[{prefix}] Electron Bot")
    @config.command(
        name="language",
        aliases=['lang']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def language(self, ctx):
        self.b.read(f"locales/{await get_lang(ctx.message)}.ini")
        embed = nextcord.Embed( 
            title=self.b.get('Bundle', 'embed.setlang.title'),
            description=self.b.get('Bundle', 'embed.choose-lang'),
            color=0x42F56C
        )
        view = SetLangButton(ctx.author.id)
        await ctx.send(embed=embed, view=view)
    @config.command(name = "mute_role")
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_guild = True)
    async def mute_role(self, ctx, role: nextcord.Role):
        self.b.read(f"locales/{await get_lang(ctx.message)}.ini")
        await MongoM().setMuteRole(ctx.guild.id, role.id)
        embed = nextcord.Embed(
            title = self.b.get('Bundle', 'embed.succerfully'),
            description = self.b.get('Bundle', 'embed.mute-role-changed').format(role.mention),
            color = 0x42F56C
        )
        await ctx.send(embed = embed)
    @config.command(name = "anti_scam")
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_guild = True)
    async def anti_scam(self, ctx, value: bool):
        self.b.read(f"locales/{await get_lang(ctx.message)}.ini")
        await MongoM().setAntiScam(ctx.guild.id, value)
        embed = nextcord.Embed(
            title = self.b.get('Bundle', 'embed.succerfully'),
            description = self.b.get('Bundle', 'embed.anti_scam-changed').format(value),
            color = 0x42F56C
        )
        await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(config(bot))