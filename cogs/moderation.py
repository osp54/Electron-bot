import asyncio
import discord
from discord.ext import commands

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self,ctx, member: discord.Member, *, reason=None):
        """
        Замьютить пользователя на сервере.
        """
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title="Замьючен", description=f"{member.mention} замьючен ", colour=discord.Colour.light_gray())
        embed.add_field(name="Причина:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"Вы были замьючены в: {guild.name} причина: {reason}")
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self,ctx, member: discord.Member):
        """
        Размьютить пользователя на сервере.
        """
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        await member.send(f"Ты был размьючен в: - {ctx.guild.name}")
        embed = discord.Embed(
            title="Размьючен!",
            description=f"**{member.name}** был размьючен модератором **{ctx.message.author}**",
            color=0x42F56C
        )
        await ctx.send(embed=embed)
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, context, member: discord.Member, *, reason="None"):
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
    @commands.command(name="idban")
    @commands.has_permissions(ban_members=True)
    async def idban(self, ctx, user_id: int, *, reason=None):
        """
        Забанить пользователя по айди.
        """
        await ctx.guild.ban(discord.Object(id=user_id), reason=reason)
        embed = discord.Embed(
              title="Пользователь забанен!",
              description=f"**{self.bot.get_user(user_id)}** был забанен модератором **{ctx.message.author}**!",
              color=0x42F56C
        )
        embed.add_field(
            name="Причина:",
            value=reason
        )
        await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, name_or_id, *, reason=None):
        """
        Разбанить пользователя на сервере.
        """
        ban = await ctx.get_ban(name_or_id)
        if not ban:
            return await ctx.send('Пользователь не найден.')
        await ctx.guild.unban(ban.user, reason=reason)
        await ctx.send(embed = discord.Embed(title='Разбанен!', description=f'Разбанен **{ban.user}** с сервера.', color=0x42F56C))
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
