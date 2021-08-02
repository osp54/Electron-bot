import discord
import os
import sys
from discord.ext import commands

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
    def restart_bot(): 
        os.execv(sys.executable, ['python'] + sys.argv)
    @commands.has_permissions(administrator=True)
    @commands.command(name="restart")
    async def restart(ctx):
        """
        Перезапустить бота.
        """
        try:
            embed = discord.Embed(
                title="Restarting...",
                description="Бот перезарускается...",
                color=0x42F56C
            )
            await ctx.send(embed=embed)
            restart_bot()
        except:
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
def setup(bot):
    bot.add_cog(main(bot))
