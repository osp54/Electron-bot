import nextcord
import json
import datetime
import humanize
from nextcord.ext import commands
from utils.misc import format_name
from nextcord.ext.commands import cooldown, BucketType
from configparser import ConfigParser

#print(bundle.get("RU", title))

class main(commands.Cog, name="main"):
    def __init__(self, bot):
        self.bot = bot
    def get_lang(client, message):
        with open("guildlang.json", "r") as f:
            guildlang = json.load(f)
        return guildlang[str(message.guild.id)]

    @commands.command()
    async def test(self, ctx):
        bundle = ConfigParser()
        bundle.read("ru.ini")
        await ctx.send(bundle.get("RU", embedTitle)
    @commands.command(
        name = "setprefix",
        usage = "`setprefix [новый префикс]`",
        aliases=['префикс']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def setprefix(self, ctx, prefix):
        """
        Изменить префикс.
        """
        if ctx.prefix == prefix:
            embed = nextcord.Embed(
                title="Ошибка",
                description="У этого сервера уже установлен такой префикс!",
                color=0xE02B2B
            )
            return await ctx.send(embed=embed)
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        await ctx.guild.me.edit(nick=f"[{prefix}] Electron Bot")
        eembed = nexcord.Embed(
            name="Успешно",
            description=f"Префикс изменен на: {ctx.prefix}",
            color=0x42F56C
        ).set_footer(text="С каждым изменением префикса, я свой никнейм меняю на `[Новый префикс] Electron Bot`!")
        await ctx.send(embed=eembed)
    @commands.command(
        name="setlang",
        usage="`setlang [язык]`",
        aliases=['язык']
    )
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
        embed = nexcord.Embed(
            name="Успешно",
            description=f"Язык изменен на: {ctx.prefix}",
            color=0x42F56C
        )
        await ctx.send(embed=embed)
    @commands.command(
        name="ping",
        usage="`ping`",
        aliases=['пинг']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ping(self, ctx):
        await ctx.send(f'Понг! {round(self.bot.latency * 1000)}ms!')
    @commands.command(
        name="avatar",
        usage="`avatar <участник>`",
        aliases=['аватар']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def avatar(self, ctx, member: nextcord.Member = None):
        """
        Получить аватар пользователя
        """
        if not member:
            member = ctx.message.author
        embed = nextcord.Embed(
            title=f"Аватар пользователя {member}",
            color=0x42F56C
        )
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)
    @commands.command(
        name="emoji",
        usage="`emoji [эмодзи]`",
        aliases=["эмодзи_инфо", "эмодзи", "эмоция", "emoteinfo"]
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def emoji(self, ctx, emoji: nextcord.Emoji):
        """
        Эмодзи.
        """
        embed = nextcord.Embed(title=f"Эмодзи {emoji.name}", color=0x42F56C)
        embed.set_thumbnail(url=emoji.url)
        embed.set_image(url=emoji.url)
        embed.add_field(name="ID", value=emoji.id)
        if emoji.user:
            embed.add_field(name="Кем добавлено", value=emoji.user)
        embed.add_field(name="Server", value=emoji.guild)
        embed.add_field(
            name="Создано",
            value=f'{nextcord.utils.format_dt(emoji.created_at, "F")} ({nextcord.utils.format_dt(emoji.created_at, "R")})',
        )
        embed.add_field(name="URL", value=f"[Здесь]({emoji.url})")
        await ctx.send(embed=embed)
    @commands.command(
        name="guild",
        usage="`guild`",
        aliases=["guildinfo", "сервер"]
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def guild(self, ctx):
        """Информация об этом сервере."""
        guild = ctx.guild
        guild_owner = self.bot.get_user(guild.owner_id)

        features = "\n".join(format_name(f) for f in guild.features)

        embed = nextcord.Embed(title=f"Сервер {guild.name}", color=0x42F56C)
        embed.add_field(name="Имя", value=guild.name)
        embed.add_field(name="ID", value=int(guild.id))
        embed.add_field(name="Owner", value=guild_owner)
        embed.add_field(name="Icon URL", value=f"[click here]({guild.icon.url})")
        embed.add_field(name="Регион", value=str(guild.region))
        embed.add_field(name="Уровень верификации", value=str(guild.verification_level))
        embed.add_field(name="Участников", value=len(guild.members))
        embed.add_field(name="Уровень бустов", value=guild.premium_tier)
        embed.add_field(name="Бустов", value=guild.premium_subscription_count)
        embed.add_field(name="Бустеров", value=len(guild.premium_subscribers))
        embed.add_field(name="Каналов", value=len(guild.channels))
        embed.add_field(name="Текстовых каналов", value=len(guild.text_channels))
        embed.add_field(name="Голосовых каналов", value=len(guild.voice_channels))
        embed.add_field(name="Категорий", value=len(guild.categories))
        embed.add_field(name="Ролей", value=len(guild.roles))
        embed.add_field(name="Эмодзи", value=f"{len(guild.emojis)}/{guild.emoji_limit}")
        embed.add_field(name="Лимит отправки", value="{round(guild.filesize_limit / 1048576)} MB")
        embed.add_field(name="Features", value=features)
        embed.set_thumbnail(url=guild.icon.url)
        await ctx.send(embed=embed)
    @commands.command(
        name="channel",
        usage="`channel <канал>`",
        aliases=['канал', 'channelinfo']
    )
    async def channel(self, ctx, channel: nextcord.TextChannel = None):
        """
        Информация о текущем/другом канале.
        """
        channel = channel or ctx.channel
        embed = nextcord.Embed(title=f"Информация об {channel.name}", color=0x42F56C)
        if channel.topic:
            embed.add_field(name="Описание", value=channel.topic, inline=False)
        embed.add_field(
            name="Создано",
            value=f'{nextcord.utils.format_dt(channel.created_at, "F")}  ({nextcord.utils.format_dt(channel.created_at, "R")})',
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
    @commands.command(
       name="poll",
       usage="poll [заголовок]",
       aliases=['опрос']
    )
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def poll(self, ctx, *, title):
        """
        Создайте опрос, в котором участники могут голосовать.
        """
        embed = nextcord.Embed(
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
