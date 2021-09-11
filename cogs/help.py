import nextcord
from utils.misc import get_lang
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
        self.b.read(f"locales/{get_lang(self.bot, ctx.message)}.ini")
        if command is None:
            embed = nextcord.Embed(title="help", color=0x2B95FF)
            text = ""
            text2 = ""
            maincog = self.bot.get_cog("main").get_commands()
            modcog = self.bot.get_cog("moderation").get_commands()
            for cmd in maincog:
                text += cmd.name + " - " + self.b.get("Bundle", f"{cmd}.description") + "\n"
            embed.add_field(name=self.b.get("Bundle", "embed.help.main"), value=text)
            for cmd in modcog:
                text2 += cmd.name + " - " + self.b.get("Bundle", f"{cmd}.description") + "\n"
            embed.add_field(name=self.b.get("Bundle", "embed.help.moderation"), value=text2)
            await ctx.send(embed=embed) 
        if command is not None:
            try:
                cmd = self.bot.get_command(command)
            except:
                eembed = nextcord.Embed(
                    title=self.b.get("Bundle", "embed.error"),
                    description=self.b.get("Bundle", "error.embed.command.not.found"),
                    color=0xFF0000
                )
                return await ctx.send(embed=eembed)
            cembed = nextcord.Embed(
                title=cmd.name.capitalize(),
                color=0x2B95FF
            ).add_field(
                name=self.b.get("Bundle", "embed.help.usage"),
                value=self.b.get("Bundle", f"{cmd}.usage")
            )
            aliase = '('
            for alias in cmd.aliases:
                aliase += f" `{alias}` "
            cembed.add_field(
                name=self.b.get("Bundle", "embed.help.aliases"),
                value=f"{aliase})"
            )
            await ctx.send(embed=cembed)
def setup(bot):
    bot.add_cog(help(bot))
