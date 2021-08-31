import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        name="mute",
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`mute [участник] <причина>`",
        aliases=['мьют', 'мут']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self,ctx, member: nextcord.Member, *, reason=None):
        """
        Замьютить пользователя на сервере.
        """
        guild = ctx.guild
        mutedRole = nextcord.utils.get(guild.roles, name="Muted")
        if ctx.author.id == member.id:
            embed = nextcord.Embed(
                title="Ошибка",
                description="Зачем? Зачем ты хочешь замьютить самого себя?",
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions.administrator:
            embed = nextcord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.top_role.position >= ctx.author.top_role.position:
            embed = nextcord.Embed(
                title='Ошибка',
                description='Вы не можете замьютить этого пользователя, так как его роль выше или на равне с вашей.',
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions > ctx.author.guild_permissions:
            embed = nextcord.Embed(
                title='Ошибка',
                description='Вы не можете замьютить этого пользователя, так как его права выше чем ваши',
                color=pxE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        try:
            await member.add_roles(mutedRole, reason=reason)
        except:
            return
        embed = nextcord.Embed(
            title="Успешно!",
            description=f"**{member.name}** замьючен модератором **{ctx.message.author}**",
            color=0x42F56C
        )
        embed.add_field(name="Причина:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
        await member.send(f"Вы были замьючены в: {ctx.message.guild} причина: {reason}")
    @commands.command(
        name="unmute",
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`unmute [участник]`",
        aliases=['размьют', 'размут']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def unmute(self,ctx, member: nextcord.Member):
        """
        Размьютить пользователя на сервере.
        """
        if ctx.author.id == member.id:
            embed = nextcord.Embed(
                title="Ошибка",
                description="Размьютить самого себя не получится.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted")
        try:
            await member.remove_roles(mutedRole)
        except:
            return
        embed = nextcord.Embed(
            title="Успешно!",
            description=f"**{member.name}** размьючен модератором **{ctx.message.author}**",
            color=0x42F56C
        )
        await ctx.send(embed=embed)
        await member.send(f"Вы были размьючены в {ctx.message.guild}!")
        await ctx.message.add_reaction('✅')
    @commands.command(
        name='kick',
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`kick [участник] <причина>`",
        aliases=['кикнуть', 'кик', 'вигнать']
        )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason="None"):
        """
        Кикнуть пользователя из сервера.
        """
        if ctx.author.id == member.id:
            embed = nextcord.Embed(
                title="Ошибка",
                description="Зачем? Зачем ты хочешь кикнуть самого себя?",
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions.administrator:
            embed = nextcord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.top_role.position >= ctx.author.top_role.position:
            embed = nextcord.Embed(
                title='Ошибка',
                description='Вы не можете выгнать этого пользователя, так как его роль выше или на равне с вашей.',
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions > ctx.author.guild_permissions:
            embed = nextcord.Embed(
                title='Ошибка',
                description='Вы не можете выгнать этого пользователя, так как его права выше чем ваши',
                color=pxE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        await member.kick(reason=f"{reason}({ctx.message.author})")
        embed = nextcord.Embed(
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
    @commands.command(
        name="ban",
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`ban [участник] <причина>`",
        aliases=['бан']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason="Причина не написана."):
        """
        Забанить пользователя на сервере.
        """
        if ctx.author.id == member.id:
            embed = nextcord.Embed(
                title="Ошибка",
                description="Зачем? Зачем ты хочешь забанить самого себя?",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if member.guild_permissions.administrator:
            embed = nextcord.Embed(
                title="Ошибка",
                description="У пользователя есть права администратора.",
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.top_role.position >= ctx.author.top_role.position:
            embed = nextcord.Embed(
                title='Ошибка',
                description='Вы не можете забанить этого пользователя, так как его роль выше или на равне с вашей.',
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions > ctx.author.guild_permissions:
            embed = nextcord.Embed(
                title='Ошибка',
                description='Вы не можете забанить этого пользователя, так как его права выше чем ваши',
                color=pxE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        try:
            await member.ban(reason=f"{reason}({ctx.message.author})")
        except:
            return
        embed = nextcord.Embed(
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
    @commands.command(
        name="idban",
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`idban [участник] <причина>`",
        aliases=['идбан', 'айдибан', 'idбан']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def idban(self, ctx, user_id: int, *, reason=None):
        """
        Забанить пользователя по айди.
        """
        if ctx.author.id == user_id:
            embed = nextcord.Embed(
                title="Ошибка",
                description="Зачем? Зачем ты хочешь забанить самого себя?",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        try:
            await ctx.guild.ban(nextcord.Object(id=user_id), reason=f"{reason}({ctx.message.author})")
        except:
            return
        embed = nextcord.Embed(
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
    @commands.command(
        name="unban",
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`unban [id забаненого]`",
        aliases=['разбан']
    )
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
        try:
            await ctx.guild.unban(ban.user, reason=reason)
        except:
            return
        await ctx.send(embed = nextcord.Embed(title='Успешно!', description=f'Разбанен **{ban.user}** с сервера.', color=0x42F56C))
        await ctx.message.add_reaction('✅')
    @commands.command(
        name="clear",
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`clear [число сообщений для удаления]`",
        aliases=['очистить']
    )
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
            embed = nextcord.Embed(
                title="Ошибка",
                description=f"`{amount}` не действительное число.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if amount < 1:
            embed = nextcord.Embed(
                title="Ошибка",
                description=f"`{amount}` не действительное число.",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        purged_messages = await ctx.message.channel.purge(limit=amount)
        embed = nextcord.Embed(
            title="Чат очищен!",
            description=f"**{ctx.message.author}** очищено **{len(purged_messages)}** сообщений!",
            color=0x42F56C
        )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
    @commands.command(
        name="clone",
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`clone <канал>`",
        aliases=["cln", "очистить"]
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def clone(self, ctx, channel: nextcord.TextChannel = None):
        """
        Клонировать текущий/другой текстовый канал.
        """
        await channel.clone(reason=f"{channel.name}({ctx.author})")
        await ctx.send("Канал <#{channel.id}> клонирован!")
    @commands.command(
        name="slowmode",
        usage="[] - обязательный аргумент.\n<> - необязательный.\n`slowmode [частота слоумода] <канал>`",
        alias=['слоумод']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def slowmode(self, ctx, slowmode: int=None, channel:nextcord.TextChannel = None):
        """
        Установить слоумод текущему/другому каналу.
        """
        if channel is None:
            channel = ctx.channel
        slowmode = max(min(slowmode, 21600), 0)
        if slowmode is None:
            embed = nextcord.Embed(
                title="Ошибка",
                description="Вам нужно упомянуть текстовый канал, чтобы установить слоумод!",
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        await channel.edit(slowmode_delay=slowmode)
        embed = nextcord.Embed(
            title="Успешно!",
            description=f"Установлен слоумод {slowmode}с.",
            color=0x00ff82
        )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
def setup(bot):
    bot.add_cog(moderation(bot))
