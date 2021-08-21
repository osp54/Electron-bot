import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

class help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="help", aliases=['хелп', 'помощь'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def help(self, context):
        """
        Список всех команд
        """
        embed = discord.Embed(title="Help", description=f"Префикс: {context.prefix}", color=0x42F56C)
        cogs = ("Main", "Moderation", "Music")
        for i in cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            command_list = [command.name for command in commands]
            command_description = [command.help for command in commands]
            help_text = '\n'.join(f'{n} - {h}' for n, h in zip(command_list, command_description))
            embed.add_field(name=i.capitalize(), value=f'```\n{help_text}\n```', inline=False)
        await context.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
