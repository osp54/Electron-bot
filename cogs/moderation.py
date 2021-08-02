
import discord
from discord.ext import commands

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mute')
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx, member: discord.Member,time):
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
        try:
            muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
            time_convert = {"s":1, "m":60, "h":3600,"d":86400}
            tempmute= int(time[0]) * time_convert[time[-1]]
        except:
            embed = discord.Embed(
                title="Ошибка",
                description="Некорректное время мьюта! Либо неизвестная ошибка.",
                color=0xE02B2B
            )
        try:
            await member.add_roles(muted_role)
            embed = discord.Embed(description= f"**{member.display_name}#{member.discriminator}** был замьючен модератором **{context.message.author}**!", color=discord.Color.green())
            await ctx.send(embed=embed, delete_after=15)
            await asyncio.sleep(tempmute)
            await member.remove_roles(muted_role)
       except:
           embed = discord.Embed(
               title="Ошибка",
               description="Похоже на то, что у человека которого вы хотите замьютить, выше роль чем у меня.",
               color=0xE02B2B
           )
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *, reason="Причина не написана."):
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
    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, context, member: discord.Member, *, reason="Причина не написана."):
        """
        Забанить пользователя на сервере.
        """
        try:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title="Ошибка",
                    description="У пользователя есть права администратора.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
            else:
                await member.ban(reason=reason)
                embed = discord.Embed(
                    title="Пользователь забанен!",
                    description=f"**{member}** был забанен модератором **{context.message.author}**!",
                    color=0x42F56C
                )
                embed.add_field(
                    name="Причина:",
                    value=reason
                )
                await context.send(embed=embed)
                await member.send(f"Вас забанил **{context.message.author}**!\nПричина: {reason}")
        except:
            embed = discord.Embed(
                title="Ошибка!",
                description="Произошла ошибка при попытке забанить пользователя. Убедитесь, что моя роль выше роли пользователя, которого вы хотите забанить.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    async def clear(self, context, amount):
        """
        Удалить несколько сообщений.
        """
        try:
            amount = int(amount)
        except:
            embed = discord.Embed(
                title="Ошибка",
                description=f"`{amount}` не действительное число.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        if amount < 1:
            embed = discord.Embed(
                title="Error!",
                description=f"`{amount}` не действительное число.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            return
        purged_messages = await context.message.channel.purge(limit=amount)
        embed = discord.Embed(
            title="Чат очищен!",
            description=f"**{context.message.author}** очищено **{len(purged_messages)}** сообщений!",
            color=0x42F56C
        )
        await context.send(embed=embed)
def setup(bot):
    bot.add_cog(moderation(bot))
