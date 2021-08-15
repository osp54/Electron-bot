import discord
import os
import sys
from discord import Embed
from config import settings
from discord.ext import commands

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="help", aliases=['хелп', 'помощь'])
    async def help(self, context):
        """
        Список всех команд
        """
        prefix = settings['prefix']
        if not isinstance(prefix, str):
            prefix = prefix[0]
        embed = discord.Embed(title="Help", description="Список доступных команд:", color=0x42F56C)
        cogs = ("Main", "Moderation")
        for i in cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            command_list = [command.name for command in commands]
            command_description = [command.help for command in commands]
            help_text = '\n'.join(f'{prefix}{n} - {h}' for n, h in zip(command_list, command_description))
            embed.add_field(name=i.capitalize(), value=f'```{help_text}```', inline=False)
        await context.send(embed=embed)
    @commands.command(name="avatar", aliases=['аватар'])
    async def avatar(self, ctx, member: discord.Member = None):
        """
        Получить аватар пользователя
        """
        if not member:
            member = ctx.message.author
        embed = discord.Embed(
            title=f"Аватар пользователя {member}",
            color=0x42F56C
        )
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
    @commands.command(name="poll", aliases=['опрос'])
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
            text=f"Опрос создан: {ctx.message.author} • Жми на реакции!"
        )
        embed_message = await ctx.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")
def setup(bot):
    bot.add_cog(main(bot))
