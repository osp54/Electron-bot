import asyncio
import discord
from discord.ext import commands

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mute')
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx, member: discord.Member, time: int, d, *, reason=None):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.add_roles(role)

                embed = discord.Embed(title="muted!", description=f"{member.mention} был замьючен модератором **{context.message.author}**!", colour=discord.Colour.light_gray())
                embed.add_field(name="Причина:", value=reason, inline=False)
                embed.add_field(name="Time:", value=f"{time}{d}", inline=False)
                await ctx.send(embed=embed)

                if d == "s":
                    await asyncio.sleep(time)

                if d == "m":
                    await asyncio.sleep(time*60)

                if d == "h":
                    await asyncio.sleep(time*60*60)

                if d == "d":
                    await asyncio.sleep(time*60*60*24)

                await member.remove_roles(role)

                embed = discord.Embed(title="unmute (temp) ", description=f"unmuted -{member.mention} ", colour=discord.Colour.light_gray())
                await ctx.send(embed=embed)

            return

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
