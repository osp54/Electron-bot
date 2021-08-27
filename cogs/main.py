import discord
import json
import datetime
import humanize
from discord.ext import commands
from functions import format_name
from discord.ext.commands import cooldown, BucketType

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['префикс'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        """
        Изменить префикс.
        """
        if ctx.prefix == prefix:
            embed = discord.Embed(
                title="Ошибка",
                description="У этого сервера уже установлен такой префикс!",
                color=0xE02B2B
            )
            await ctx.send(embed=embed)
            return
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await ctx.guild.me.edit(nick=f"[{prefix}] Electron Bot")
        await ctx.send(f"Prefix changed to: {prefix}")
    @commands.command(aliases=['язык'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def setlang(self, ctx, lang):
        """
        Изменить язык бота.
        """
        with open("guildlang.json", "r") as f:
            guildlang = json.load(f)
        guildlang[str(ctx.guild.id)] = lang
        with open("guildlang.json", "w") as f:
            json.dump(guildlang, f, indent=4)
        await ctx.send(f"Prefix changed to: {lang}")
    @commands.command(name="avatar", aliases=['аватар'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member = None):
        """
        Получить аватар пользователя
        """
        if not member:
            member = ctx.message.author
        embed = discord.Embed(
            title=f"Аватар пользователя {member}",
            color=0x42F56C
        )
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
    @commands.command(aliases=["эмодзи_инфо", "emoteinfo"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def emoji(self, ctx, emoji: discord.Emoji):
        """
        Эмодзи.
        """
        embed = discord.Embed(title=f"Эмодзи {emoji.name}", description="\\" + str(emoji))
        embed.set_thumbnail(url=emoji.url)
        embed.set_image(url=emoji.url)
        embed.add_field(name="ID", value=emoji.id)
        if emoji.user:
            embed.add_field(name="Кем добавлено", value=emoji.user)
        embed.add_field(name="Server", value=emoji.guild)
        embed.add_field(
            name="Создано",
            value=f'{discord.utils.format_dt(emoji.created_at, "F")} ({discord.utils.format_dt(emoji.created_at, "R")})',
        )
        embed.add_field(name="URL", value=f"[Здесь]({emoji.url})")
        await ctx.send(embed=embed)
    @commands.command(aliases=["guildinfo", "сервер"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def serverinfo(self, ctx):
        """Информация об этом сервере."""
        guild = ctx.guild
        guild_owner = self.bot.get_user(guild.owner_id)

        features = "\n".join(format_name(f) for f in guild.features)

        embed = discord.Embed(
            title=f"Сервер {guild.name}",
            description=(
                f"Имя: {guild.name}\n"
                f"Создан: {discord.utils.format_dt(guild.created_at, 'F')} ({discord.utils.format_dt(guild.created_at, 'R')})"
                f"ID: {guild.id}\nOwner: {guild_owner}\n"
                f"Icon URL: [click here]({guild.icon.url})\n"
                f"Регион: {str(guild.region)}\n"
                f"Уровень верификации: {str(guild.verification_level)}\n"
                f"Участников: {len(guild.members)}\n"
                f"Уровень бустов: {guild.premium_tier}\n"
                f"Бустов: {guild.premium_subscription_count}\n"
                f"Бустеров: {len(guild.premium_subscribers)}\n"
                f"Каналов: {len(guild.channels)}\n"
                f"Текстовых каналов: {len(guild.text_channels)}\n"
                f"Голосовых каналов: {len(guild.voice_channels)}\n"
                f"Категорий: {len(guild.categories)}\n"
                f"Ролей: {len(guild.roles)}\n"
                f"Эмодзи: {len(guild.emojis)}/{guild.emoji_limit}\n"
                f"Лимит отправки: {round(guild.filesize_limit / 1048576)} MB\n"
                f"**Features:** {features}"
            ),
        )
        embed.set_thumbnail(url=guild.icon.url)
        await ctx.send(embed=embed)
    @commands.command(aliases=['ci', 'канал'])
    async def channelinfo(self, ctx, channel: discord.TextChannel = None):
        """
        Информация о текущем/другом канале.
        """
        channel = channel or ctx.channel
        embed = discord.Embed(title=f"Информация об {channel.name}", color=0x42F56C)
        if channel.topic:
            embed.add_field(name="Описание", value=channel.topic, inline=False)
        embed.add_field(
            name="Создано",
            value=f'{discord.utils.format_dt(channel.created_at, "F")}  ({discord.utils.format_dt(channel.created_at, "R")})',
        )
        embed.add_field(name="ID", value=channel.id)
        embed.add_field(name="Тип", value=channel.type)
        embed.add_field(name="Позиция", value=f"{channel.position}/{len(ctx.guild.text_channels)}")
        embed.add_field(name="Категория", value=channel.category.name)
        if channel.slowmode_delay:
            embed.add_field(
                name="Слоумод",
                value=f"{channel.slowmode_delay} секунд ({humanize.naturaldelta(datetime.timedelta(seconds=int(channel.slowmode_delay)))})",
            )
        
        await ctx.send(embed=embed)
    @commands.command(name="poll", aliases=['опрос'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def poll(self, ctx, *, title):
        """
        Создайте опрос, в котором участники могут голосовать.
        """
        embed = discord.Embed(
            title="Создан новый опрос!",
            description=f"{title}",
            color=0x42F56C
        )
        embed.set_footer(
            text=f"Опрос создан: {ctx.message.author} • Жми на реакции!"
        )
        embed_message = await ctx.send(embed=embed)
        await embed_message.add_reaction("👍")
        await embed_message.add_reaction("👎")
        await embed_message.add_reaction("🤷")
def setup(bot):
    bot.add_cog(main(bot))
