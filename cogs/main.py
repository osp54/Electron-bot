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
    @commands.command(name="serverinfo",aliases=['server'])
    async def serverinfo(self, ctx):
        """
        Информация о сервере.
        """
        guild = ctx.guild
        guild_age = (ctx.message.created_at - guild.created_at).days
        created_at = f"Сервер создан {guild.created_at.strftime('%b %d %Y at %H:%M')}. Это больше {guild_age} дней назад!"
        color = discord.Color.green()

        em = discord.Embed(description=created_at, color=color)
        em.add_field(name='Участников онлайн', value=len({m.id for m in guild.members if m.status is not discord.Status.offline}))
        em.add_field(name='Всего участников', value=len(guild.members))
        em.add_field(name='Текстовых каналов', value=len(guild.text_channels))
        em.add_field(name='Голосовые каналов', value=len(guild.voice_channels))
        em.add_field(name='Ролей', value=len(guild.roles))
        em.add_field(name='Создатель', value=guild.owner)
        icon = str(ctx.guild.icon_url)
        em.set_thumbnail(url=icon)
        em.set_author(name=guild.name, icon_url=icon)
        await ctx.send(embed=em)
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
