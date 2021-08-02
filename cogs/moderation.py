
import discord
from discord.ext import commands

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mute')
    @commands.has_permissions(kick_members=True)
    async def mute(ctx, member: discord.Member):
        try:
            role = discord.utils.get(member.server.roles, name='Muted')
            await ctx.add_roles(member, role)
            embed=discord.Embed(title="Юзер замьючен!", description="**{0}** был замьючен модератором**{1}**!".format(member, ctx.message.author), color=0xff00f6)
            await ctx.send(embed=embed)
        except:
            await ctx.send("У вас недостаточно прав для этой команды.")
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *, reason="Not specified"):
        """
        Кикнуть пользователя из сервера.
        """
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
        else:
            try:
                await member.kick(reason=reason)
                embed = discord.Embed(
                    title="User Kicked!",
                    description=f"**{member}** был кикнут модератором **{context.message.author}**!",
                    color=0x42F56C
                )
                embed.add_field(
                    name="Причина:",
                    value=reason
                )
                await context.send(embed=embed)
                try:
                    await member.send(
                        f"Вас кикнул **{context.message.author}**!\nПричина: {reason}"
                    )
                except:
                    pass
            except:
                embed = discord.Embed(
                    title="Ошибка!",
                    description="Произошла ошибка при попытке кикнуть пользователя. Убедитесь, что моя роль выше роли пользователя, которого вы хотите кикнуть.",
                    color=0xE02B2B
                )
                await context.message.channel.send(embed=embed)
def setup(bot):
    bot.add_cog(moderation(bot))
