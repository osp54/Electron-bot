import nextcord
import random
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType
colors = ['0xBADD02', '0x10DD02', '0x02DDDC', '0x1466E1', '0xFF0000', 'CA0EAC', 'CA770E']
color = random.choice(colors)
class help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="help", aliases=['хелп', 'помощь'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def help(self, ctx, command = None):
        """
        Список всех команд
        """
        if command is None:
            embed = nextcord.Embed(title="Список доступных команд",  color=color)
            embed.add_field(name="Префикс", value=ctx.prefix)
            cogs = ("Main", "Moderation", "Music")
            for i in cogs:
                cog = self.bot.get_cog(i.lower())
                commands = cog.get_commands()
                command_list = [command.name for command in commands]
                command_description = [command.help for command in commands]
                help_text = '\n'.join(f'`{n}` - {h}' for n, h in zip(command_list, command_description))
                embed.add_field(name=i.capitalize(), value=f'{help_text}', inline=False)
            embed.set_footer(text=f'Запрошено: {ctx.author.display_name}')
            await ctx.send(embed=embed)
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
            color=color
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
