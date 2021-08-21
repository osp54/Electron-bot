import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="mute", aliases=['мьют', 'мут'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self,ctx, member: discord.Member, *, reason=None):
        """
        Замьютить пользователя на сервере.
        """
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
       # if ctx.author.id == member.id:
       #     embed = discord.Embed(
       #         title="Ошибка",
       #         description="Зачем? Зачем ты хочешь замьютить самого себя?",
       #         color=0xE02B2B
       #     )
       #     await ctx.send(embed=embed)
       #     await ctx.message.add_reaction('❌')
       #     return
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
        mute = await member.add_roles(mutedRole, reason=reason)
        if not mute:
            return
        embed = discord.Embed(
            title="Успешно!",
            description=f"**{member.name}** замьючен модератором **{ctx.message.author}**",
            color=0x42F56C
        )
        embed.add_field(name="Причина:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
        await member.send(f"Вы были замьючены в: {ctx.message.guild} причина: {reason}")
    @commands.command(name="unmute", aliases=['размьют', 'размут'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(manage_roles=True)
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
        if not mutedRole:
            return await ctx.send("Пожалуйста, создайте роль **Muted**!")
        unmute = await member.remove_roles(mutedRole)
        if unmute:
            embed = discord.Embed(
                title="Успешно!",
                description=f"**{member.name}** размьючен модератором **{ctx.message.author}**",
                color=0x42F56C
            )
            await ctx.send(embed=embed)
            await member.send(f"Вы были размьючены в {ctx.message.guild}!")
            await ctx.message.add_reaction('✅')
    @commands.command(name='kick', aliases=['кикнуть', 'кик', 'вигнать'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(kick_members=True)
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
        kick = await member.kick(reason=f"{reason}({ctx.message.author})")
        if kick:
            embed = discord.Embed(
                title="Успешно!",
                description=f"**{member}** кикнут модератором **{ctx.message.author}**!",
                color=0x42F56C
            )
            embed.add_field(
                name="Причина:",
                value=reason
            )
            await ctx.send(embed=embed)
            await member.send(f"Вы были кикнуты в {ctx.message.guild}, модератором {ctx.message.author}!")
            await ctx.message.add_reaction('✅')
    @commands.command(name="ban", aliases=['бан'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members=True)
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
        ban = await member.ban(reason=f"{reason}({ctx.message.author})")
        if ban:
            embed = discord.Embed(
                title="Успешно!",
                description=f"**{member}** был забанен модератором **{ctx.message.author}**!",
                color=0x42F56C
            )
            embed.add_field(
                name="Причина:",
                value=reason
            )
            await context.send(embed=embed)
            await ctx.message.add_reaction('✅')
            await member.send(f"Вас забанил **{context.message.author}**!\nПричина: {reason}")
    @commands.command(name="idban", aliases=['идбан', 'айдибан', 'idбан'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members=True)
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
        idban = await ctx.guild.ban(discord.Object(id=user_id), reason=f"{reason}({ctx.message.author})")
        if idban:
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
    @commands.command(name="unban", aliases=['разбан'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, name_or_id, *, reason=None):
        """
        Разбанить пользователя на сервере.
        """
        ban = await ctx.get_ban(name_or_id)
        if not ban:
            return await ctx.send('Пользователь не найден.')
        unban = await ctx.guild.unban(ban.user, reason=reason)
        if unban:
            await ctx.send(embed = discord.Embed(title='Успешно!', description=f'Разбанен **{ban.user}** с сервера.', color=0x42F56C))
            await ctx.message.add_reaction('✅')
    @commands.command(name="clear", aliases=['очистить'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    async def clear(self, ctx, amount):
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
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if amount < 1:
            embed = discord.Embed(
                title="Ошибка",
                description=f"`{amount}` не действительное число.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        purged_messages = await ctx.message.channel.purge(limit=amount)
        embed = discord.Embed(
            title="Чат очищен!",
            description=f"**{ctx.message.author}** очищено **{len(purged_messages)}** сообщений!",
            color=0x42F56C
        )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
def setup(bot):
    bot.add_cog(moderation(bot))
