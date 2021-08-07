import discord
import os
import sys
from discord import Embed
from config import settings
from discord.ext import commands

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
    def restart_bot(): 
        os.execv(sys.executable, ['python'] + sys.argv)
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
    @commands.has_permissions(administrator=True)
    @commands.command(name="restart")
    async def restart(self,ctx):
        """
        Перезапустить бота.
        """
        try:
            embed = discord.Embed(
                title="Restarting...",
                description="Бот перезапускается...",
                color=0x42F56C
            )
            await ctx.send(embed=embed)
            restart_bot()
        except discord.ext.commands.errors.MissingPermissions:
            embed = discord.Embed(
                title="Ошибка",
                description="На эту команду право имеют только люди с правом администратор!",
                color=0xFFFFF
            )
            ctx.send(embed=embed)
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        """
        Получить аватар пользователя
        """
        if member == 'None':
            member = ctx.author
        embed = discord.Embed(
            title=f"Аватар пользователя {member}",
            color=0x42F56C
        )
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
    @commands.command(name="poll")
    async def poll(self, ctx, *, title):
        """
        Создайте опрос, в котором участники могут голосовать.
        """
        embed = discord.Embed(
            title="Создан новый опрос!",
            description=f"{title}",
            color=0x42F56C
        )
        embed.set_footer(
            text=f"Опрос создан: {context.message.author} • Жми на реакции!"
        )
        embed_message = await ctx.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed = discord.Embed(title='Ошибка', description=f'**{ctx.author.name}**, У вас нет прав для использования этой команды.', color=0xFF0000))
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed = discord.Embed(title='Ошибка', description=f'У этой команды кулдавн! Пожалуйста подождите {error.retry_after:.2f}s', color=0xFF0000))
        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.send(f"{ctx.author.mention}, У бота нет прав на это. Пожалуйста, дайте боту правильные права")
        else:
           channel = self.bot.get_channel(872078345137979434)
           error = getattr(error, 'original', error)
           if hasattr(ctx.command, 'on_error'):
                return

           if ctx.cog:
               if ctx.cog._get_overridden_method(ctx.cog.cog_command_error) is not None:
                   return
           embed = Embed(
               title="New Error",
               description=f"Command: {ctx.command.name}\n\nUsername: `{ctx.author}`\n\nUserID: `{ctx.author.id}`\n\nGuild Name: `{ctx.guild.name}`",
               color=0x42F56C
           )
           embed.add_field(
                   name="Error:",
                   value=f"```\n{ctx.author} - {error}\n```"
           )
           await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(main(bot))
