import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="help", aliases=['хелп', 'помощь'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def help(self, ctx):
        """
        Список всех команд
        """
        embed = nextcord.Embed(title="Список доступных команд",  color=0x42F56C)
        embed.add_field(name="Префикс", value=ctx.prefix)
        cogs = ("Main", "Moderation", "Music")
        for i in cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            command_list = [command.name for command in commands]
            command_description = [command.help for command in commands]
            help_text = '\n'.join(f'`{n}` - {h}' for n, h in zip(command_list, command_description))
            embed.add_field(name=i.capitalize(), value=f'{help_text}', inline=False)
        embed.set_footer(text=f'Запрошено: {ctx.author.name}')
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(help(bot))
