import discord
from discord.ext import commands
from config import settings
class fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='embed')
    @commands.has_permissions(manage_messages=True)
    async def embed(self, ctx,*, message="No Arguments"):
        """
        Отправить эмбед сообщение
        """
        await ctx.message.delete()
        embed=discord.Embed()
        embed.add_field(name="Embed", value=f"{message}", inline=False)
        await ctx.send(embed=embed)
    @commands.command(name='say')
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx,*, message=None):
        """
        Отправить сообщение от имени бота
        """
        await ctx.message.delete()
        await ctx.send(message)
    @commands.command(name="help")
    async def help(self, context):
        """
        Список всех команд
        """
        prefix = settings['prefix']
        if not isinstance(prefix, str):
            prefix = prefix[0]
        embed = discord.Embed(title="Help", description="Список доступных команд:", color=0x42F56C)
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            command_list = [command.name for command in commands]
            command_description = [command.help for command in commands]
            help_text = '\n'.join(f'{prefix}{n} - {h}' for n, h in zip(command_list, command_description))
            embed.add_field(name=i.capitalize(), value=f'```{help_text}```', inline=False)
        await context.send(embed=embed)

def setup(bot):
    bot.add_cog(fun(bot))
