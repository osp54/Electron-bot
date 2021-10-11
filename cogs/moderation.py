import nextcord
import motor.motor_asyncio.motor_asyncio
from utils.misc import get_lang
from configparser import ConfigParser
from nextcord.ext import commands
from nextcord.ext.commands import cooldown, BucketType

class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot
        self.client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://electron:W$2ov3b$Fff58ludgg@cluster.xyknx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.collg = self.client.electron.guilds
        self.b = ConfigParser() # b - bundle
    @commands.command(
        name="mute",
        aliases=['мьют', 'мут']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self,ctx, member: nextcord.Member, *, reason="Not Specified"):
        guild = ctx.guild
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        res = await self.collg.find_one({"_id": guild.id})
        try:
            mutedRole = ctx.guild.get_role(res[mute_role])
        except:
            mutedRole = nextcord.utils.get(guild.roles, name="Electron Mute")
            if not mutedRole:
                mutedRole = await guild.create_role(name="Electron Mute")
                for channel in guild.channels:
                    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
        if ctx.author.id == member.id:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.mute.why-mute-myself'),
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions.administrator:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.mute.user-has-admin-perm'),
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.top_role.position >= ctx.author.top_role.position:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.mute.role-above-or-equal'),
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions > ctx.author.guild_permissions:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.mute.role-above'),
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if not mutedRole:
            mutedRole = await guild.create_role(name="Electron Mute")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        try:
            await member.add_roles(mutedRole, reason=reason)
        except:
            return
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.mute.description').format(member.name),
            color=0x42F56C
        )
        embed.add_field(name=self.b.get('Bundle', 'embed.moderator'), value=ctx.message.author)
        embed.add_field(name=self.b.get('Bundle', 'embed.reason'), value=reason, inline=False)
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
        await member.send(self.b.get('Bundle', 'mute.pm-message').format(ctx.message.guild, ctx.author))
    @commands.command(
        name="unmute",
        aliases=['размьют', 'размут']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def unmute(self,ctx, member: nextcord.Member):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        if ctx.author.id == member.id:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.unmute.not-unmute-myself'),
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        mutedRole = nextcord.utils.get(ctx.guild.roles, name="Electron Mute")
        try:
            await member.remove_roles(mutedRole)
        except:
            return
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.unmute.unmuted').format(member),
            color=0x42F56C
        ).add_field(name=self.b.get('Bundle', 'embed.moderator'), value=ctx.message.author)
        await ctx.send(embed=embed)
        await member.send(self.b.get('Bundle', 'embed.unmute.pm-message').format(ctx.message.guild))
        await ctx.message.add_reaction('✅')
    @commands.command(
        name='kick',
        aliases=['кикнуть', 'кик', 'вигнать']
        )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason="Not Specified"):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        if ctx.author.id == member.id:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.kick.why-kick-myself'),
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.top_role.position >= ctx.author.top_role.position:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.kick.role-above-or-equal'),
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions > ctx.author.guild_permissions:
            embed = nextcord.Embed(
                title='Ошибка',
                description=self.b.get('Bundle', 'embed.error.kick.role-above'),
                color=pxE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        await member.kick(reason=f"{reason}({ctx.message.author})")
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.kick.kicked').format(member),
            color=0x42F56C
        ).add_field(
            name=self.b.get('Bundle', 'embed.moderator'),
            value=ctx.message.author
        ).add_field(
            name=self.b.get('Bundle', 'embed.reason'),
            value=reason
        )
        await ctx.send(embed=embed)
        await member.send(self.b.get('Bundle', 'kick.pm-message').format(ctx.message.guild, ctx.message.author))
        await ctx.message.add_reaction('✅')
    @commands.command(
        name="ban",
        aliases=['бан']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason="Not Specified"):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        if ctx.author.id == member.id:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.ban.why-ban-myself'),
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            await ctx.message.add_reaction('❌')
            return
        if member.top_role.position >= ctx.author.top_role.position:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.ban.role-above-or-equal'),
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        if member.guild_permissions > ctx.author.guild_permissions:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.error.ban.role-above'),
                color=0xE02B2B
            )
            await ctx.message.add_reaction('❌')
            return await ctx.send(embed=embed)
        try:
            await member.ban(reason=f"{reason}({ctx.message.author})")
        except:
            return
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.ban.baned').format(member),
            color=0x42F56C
        ).add_field(
            name=self.b.get('Bundle', 'embed.reason'),
            value=reason
        ).add_field(
            name=self.b.get('Bundle', 'embed.moderator'),
            value=ctx.author
        )
        await context.send(embed=embed)
        await ctx.message.add_reaction('✅')
        await member.send(self.b.get('Bundle', 'embed.ban.pm-message').format(ctx.guild, ctx.author))
    @commands.command(
        name="idban",
        aliases=['идбан', 'айдибан', 'idбан']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def idban(self, ctx, user_id: int, *, reason=None):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        if ctx.author.id == user_id:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.ban.why-ban-myself'),
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
              title=self.b.get('Bundle', 'embed.succerfully'),
              description=self.b.get('Bundle', 'embed.ban.baned').format(self.bot.get_user(user_id).name),
              color=0x42F56C
        ).add_field(
            name=self.b.get('Bundle', 'embed.reason'),
            value=reason
        ).add_field(
            name=self.b.get('Bundle', 'embed.moderator'),
            value=ctx.author
        )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
    @commands.command(
        name="unban",
        aliases=['разбан']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, name_or_id, *, reason=None):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        ban = await ctx.get_ban(name_or_id)
        if not ban:
            return await ctx.send(self.b.get('Bundle', 'embed.user-not-found'))
        try:
            await ctx.guild.unban(ban.user, reason=reason)
        except:
            return
        await ctx.send(embed = nextcord.Embed(
            title=self.bot.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.user-was-unbaned').format(ban.user),
            color=0x42F56C
            )
        )
        await ctx.message.add_reaction('✅')
    @commands.command(
        name="clear",
        aliases=['очистить']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    async def clear(self, ctx, amount):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        try:
            amount = int(amount)
        except:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.clear.not-amount').format(amount),
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            return await ctx.message.add_reaction('❌')
        if amount < 1:
            embed = nextcord.Embed(
                title=self.b.get('Bundle', 'embed.error'),
                description=self.b.get('Bundle', 'embed.clear.not-amount').format(amount),
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            return await ctx.message.add_reaction('❌')
        purged_messages = await ctx.message.channel.purge(limit=amount)
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.clear.purged').format(ctx.author, len(purged_messages)),
            color=0x42F56C
        )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
    @commands.command(
        name="clone",
        aliases=["клон"]
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def clone(self, ctx, channel: nextcord.TextChannel = None):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        if channel is None:
            channel = ctx.channel
        await channel.clone(reason=ctx.author)
        await ctx.send(self.b.get('Bundle', 'embed.clone.cloned').format(channel.mention))
    @commands.command(
        name="slowmode",
        alias=['слоумод']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def slowmode(self, ctx, slowmode: int=None, channel:nextcord.TextChannel = None):
        self.b.read(f"locales/{get_lang(ctx.message)}.ini")
        if channel is None:
            channel = ctx.channel
        slowmode = max(min(slowmode, 21600), 0)
        await channel.edit(slowmode_delay=slowmode)
        embed = nextcord.Embed(
            title=self.b.get('Bundle', 'embed.succerfully'),
            description=self.b.get('Bundle', 'embed.slowmode.done').format(slowmode),
            color=0x00ff82
        )
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('✅')
def setup(bot):
    bot.add_cog(moderation(bot))
