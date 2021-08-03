import discord
import os
import sys
from discord import Embed
from discord.ext import commands

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
    def restart_bot(): 
        os.execv(sys.executable, ['python'] + sys.argv)
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
    @commands.command(name="poll")
    async def poll(self, context, *, title):
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
        embed_message = await context.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        channel = self.bot.get_channel(872078345137979434)
        error = getattr(error, 'original', error)
        channel.send(error)
        if hasattr(ctx.command, 'on_error'):
            return

        if ctx.cog:
            if ctx.cog._get_overridden_method(ctx.cog.cog_command_error) is not None:
                return

        embed = Embed(
            title="New error",
            description=f"Name: {ctx.author}, ID: {ctx.author.id}",
            color=0x42F56C
        )
        embed.add_field(
                name="INFO:",
                value=f"CMD: `{ctx.command.name}`"
        )
        embed.add_field(
                name="ERROR:",
                value=f"```\n{ctx.author} - {error}\n```"
        )
        await channel.send(embed=embed)
def setup(bot):
    bot.add_cog(main(bot))
