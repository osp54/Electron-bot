import nextcord
from utils.misc import get_lang
from configparser import ConfigParser
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="help", aliases=['хелп', 'помощь'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def help(self, ctx, command = None):
        """
        Список всех команд
        """
        bundle = ConfigParser()
        bundle.read(f"{get_lang(self.bot, ctx.message)}.ini")
        if command is None:
            embed = nextcord.Embed(title="Список доступных команд",  color=0x2B95FF)
            embed.add_field(name="Префикс", value=ctx.prefix)
            cogs = ("main", "moderation", "music")
            for i in cogs:
                cog = self.bot.get_cog(i)
            commands = cog.get_commands()
            #bundle.get("Bundle", f"{command}Description")
            for command in commands:
                commands_list = '( '
                commands_list += f'`{command}`, )'
            embed.add_field(name=bundle.get("Bundle", "helpCommandsEmbed"), value=commands_list, inline=False)
            embed.set_footer(text=f'Запрошено: {ctx.author.display_name}')
            await ctx.send(embed=embed)
        if command is not None:
            try:
                cmd = self.bot.get_command(command)
            except:
                eembed = nextcord.Embed(
                    title="Ошибка",
                    description="Команда не найдена 🧐",
                    color=0xFF0000
                )
                return await ctx.send(embed=eembed)
            cembed = nextcord.Embed(
                title=cmd.name.capitalize(),
                color=0x2B95FF
            ).add_field(
                name="Использование",
                value=cmd.usage
            )
            aliase = '('
            for alias in cmd.aliases:
                aliase += f" `{alias}` "
            cembed.add_field(
                name="Алиасы(под-имена)",
                value=f"{aliase})"
            )
            await ctx.send(embed=cembed)
def setup(bot):
    bot.add_cog(help(bot))
