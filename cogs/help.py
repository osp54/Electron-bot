import nextcord
from utils.misc import get_lang, get_prefix2, cmdInfo
from configparser import ConfigParser
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot
        self.b = ConfigParser()
    @commands.command(name="help", aliases=['хелп', 'помощь'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def help(self, ctx, command = None):
        """
        Список всех команд
        """
        self.b.read(f"locales/{await get_lang(ctx.message)}.ini")
        if command is None:
            embed = nextcord.Embed(title=self.b.get("Bundle", "embed.help.title"), description=self.b.get("Bundle", "embed.help.description"), color=0x2B95FF)
            prefix = await get_prefix2(self.bot, ctx.message, True)
            text = ""
            text2 = ""
            text3 = ""
            maincog = self.bot.get_cog("main").get_commands()
            modcog = self.bot.get_cog("moderation").get_commands()
            configcog = self.bot.get_cog("config").get_commands()
            for cmd in maincog:
                text += prefix + cmd.name + " **| **`" + self.b.get('Bundle', f'{cmd}.usage') + "`** |**\n" + self.b.get('Bundle', f'{cmd}.description') + "\n\n"
            embed.add_field(name=self.b.get("Bundle", "embed.help.main"), value=text)
            for cmd in modcog:
                text2 += prefix + cmd.name + " **| **`" + self.b.get('Bundle', f'{cmd}.usage') + "`** |**\n" + self.b.get('Bundle', f'{cmd}.description') + "\n\n"
            embed.add_field(name=self.b.get("Bundle", "embed.help.moderation"), value=text2)
            for cmd in configcog:
                text3 += prefix + cmd.name + " **| **`" + self.b.get('Bundle', f'{cmd}.usage') + "`** |**\n" + self.b.get('Bundle', f'{cmd}.description') + "\n\n"
            embed.add_field(name=self.b.get("Bundle", "embed.help.config"), value=text3)
            await ctx.send(embed=embed) 
        if command is not None:
            await cmdInfo(ctx, self, command)
def setup(bot):
    bot.add_cog(help(bot))
