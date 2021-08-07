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
        if ctx.author.id == member.id:
            embed = discord.Embed(
                title="Ошибка",
                description="Зачем? Зачем ты хочешь замьютить самого себя?",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title="Успешно!", description=f"{member.mention} замьючен ", colour=discord.Colour.light_gray())
        embed.add_field(name="Причина:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"Вы были замьючены в: {guild.name} причина: {reason}")
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self,ctx, member: discord.Member):
        """
        Размьютить пользователя на сервере.
        """
        if ctx.author.id == member.id:
            embed = discord.Embed(
                title="Ошибка",
                description="Размьютить самого себя не получится.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        embed = discord.Embed(
            title="Успешно!",
            description=f"**{member.name}** был размьючен модератором **{ctx.message.author}**",
            color=0x42F56C
        )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="None"):
        """
        Кикнуть пользователя из сервера.
        """
        if ctx.author.id == member.id:
            embed = discord.Embed(
                title="Ошибка",
                description="Зачем? Зачем ты хочешь кикнуть самого себя?",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="Успешно!",
                description=f"**{member}** был кикнут модератором **{context.message.author}**!",
                color=0x42F56C
            )
            embed.add_field(
                name="Причина:",
                value=reason
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('✅')
    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Причина не написана."):
        """
        Забанить пользователя на сервере.
        """
        if ctx.author.id == member.id:
            embed = discord.Embed(
                title="Ошибка",
                description="Зачем? Зачем ты хочешь забанить самого себя?",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if member.guild_permissions.administrator:
            embed = discord.Embed(
            title="Ошибка",
            description="У пользователя есть права администратора.",
            color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="Успешно!",
                description=f"**{member}** был забанен модератором **{context.message.author}**!",
                color=0x42F56C
            )
            embed.add_field(
                name="Причина:",
                value=reason
            )
            await context.send(embed=embed)
            await ctx.message.add_reaction('✅')
            await member.send(f"Вас забанил **{context.message.author}**!\nПричина: {reason}")
    @commands.command(name="idban")
    @commands.has_permissions(ban_members=True)
    async def idban(self, ctx, user_id: int, *, reason=None):
        """
        Забанить пользователя по айди.
        """
        if ctx.author.id == user_id:
            embed = discord.Embed(
                title="Ошибка",
                description="Зачем? Зачем ты хочешь забанить самого себя?",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if member.guild_permissions.administrator:
            embed = discord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        await ctx.guild.ban(discord.Object(id=user_id), reason=reason)
        embed = discord.Embed(
              title="Успешно!",
              description=f"**{self.bot.get_user(user_id)}** был забанен модератором **{ctx.message.author}**!",
              color=0x42F56C
        )
        embed.add_field(
            name="Причина:",
            value=reason
        )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
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
        await ctx.send(embed = discord.Embed(title='Успешно!', description=f'Разбанен **{ban.user}** с сервера.', color=0x42F56C))
        await ctx.message.add_reaction('✅')
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
            await context.message.add_reaction('❌')
            return
        if amount < 1:
            embed = discord.Embed(
                title="Ошибка",
                description=f"`{amount}` не действительное число.",
                color=0xE02B2B
            )
            await context.send(embed=embed)
            await context.message.add_reaction('❌')
            return
        purged_messages = await context.message.channel.purge(limit=amount)
        embed = discord.Embed(
            title="Чат очищен!",
            description=f"**{context.message.author}** очищено **{len(purged_messages)}** сообщений!",
            color=0x42F56C
        )
        await context.send(embed=embed)
        await ctx.message.add_reaction('✅')
def setup(bot):
    bot.add_cog(moderation(bot))
