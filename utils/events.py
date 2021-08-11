import discord
from discord.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
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
    bot.add_cog(events(bot))